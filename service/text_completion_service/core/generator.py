from text_completion_service.singleton import Singleton
from text_completion_service.__main__ import app
from text_completion_service.core.config import MODEL_NAME, LOAD_IN_8BIT, NUM_RETURN_SEQ, TOP_K, TOP_P, DO_SAMPLE, \
    EARLY_STOPPING

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch



class TextGenerator(metaclass=Singleton):
    """
    Base class for the text generator using singleton
    """

    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto", load_in_8bit=LOAD_IN_8BIT,
                                                          torch_dtype=torch.float16)
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

        app.app.logger.warning("Model Loaded")

    def predict(self, prompt, suggestion_len=11, num_return_sequences=NUM_RETURN_SEQ, top_k=TOP_K, top_p=TOP_P,
                do_sample=DO_SAMPLE, early_stopping=EARLY_STOPPING):
        r"""
        Generate text completion candidates for the given prompt

        Args:

        prompt: `str`, textual prompt to complete
        suggestion_len: `int`, maximum number of token generate in the text completion suggestions
        num_return_sequences: `int` number of text completion suggestion to return
        top_k: `int` the number of highest probability vocabulary tokens to keep for top-k-filtering.
        top_p: `float`, if set to float < 1, only the most probable tokens with probabilities that add up to `top_p`
                or higher are kept for generation.
        do_sample: `bool`, whether or not to use sampling ; use greedy decoding otherwise.
        early_stopping: `bool`, whether to stop the beam search when at least `num_beams` sentences are finished per
                        batch or not.

        Returns: `List[str]` list of the text completion suggetions

        """
        encoding = self.tokenizer.encode_plus(prompt, return_tensors="pt")
        input_ids, attention_masks = encoding["input_ids"].to(self.device), encoding["attention_mask"].to(self.device)

        outputs = self.model.generate(
            input_ids=input_ids, attention_mask=attention_masks,
            max_length=input_ids.shape[1] + suggestion_len,
            do_sample=do_sample,
            top_k=top_k,
            top_p=top_p,
            early_stopping=early_stopping,
            num_return_sequences=num_return_sequences
        )

        return self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
