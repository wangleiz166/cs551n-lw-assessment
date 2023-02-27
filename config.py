import openai
import base64

decoded_bytes = base64.b64decode("c2stZFBuclVrUTl6a240SzlqZ1FxR2pUM0JsYmtGSmZsTUtjNUtkUUc5U1R2WmZ1Zk9N")
decoded_str = decoded_bytes.decode('utf-8')

openai.api_key = decoded_str

