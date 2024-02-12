
pip install -U -q google-generativeai

# Install the client library and import necessary modules.
import google.generativeai as genai

"""## Set the API key

Add your API_KEY to the secrets manager in the left pannel "🔑".
"""

from google.colab import userdata
secretName='AIzaSyBdinIc1IpTeI_QF8A3LIyhZOTGsQQ1HIM'
API_KEY=userdata.get('secretName')

# Configure the client library by providing your API key.
genai.configure(api_key=API_KEY)

"""### Parse the arguments"""

model = 'gemini-pro' # @param {isTemplate: true}
contents_b64 = 'W3sicGFydHMiOlt7InRleHQiOiJDYW4geW91IGhlbHAgYnVpbGQgYSBtb2RlbCB0byBpZGVudGlmeSB3aGljaCBlc3NheSB3YXMgd3JpdHRlbiBieSBtaWRkbGUgYW5kIGhpZ2ggc2Nob29sIHN0dWRlbnRzLCBhbmQgd2hpY2ggd2FzIHdyaXR0ZW4gdXNpbmcgYSBsYXJnZSBsYW5ndWFnZSBtb2RlbD8gV2l0aCB0aGUgc3ByZWFkIG9mIExMTXMsIG1hbnkgcGVvcGxlIGZlYXIgdGhleSB3aWxsIHJlcGxhY2Ugb3IgYWx0ZXIgd29yayB0aGF0IHdvdWxkIHVzdWFsbHkgYmUgZG9uZSBieSBodW1hbnMuIEVkdWNhdG9ycyBhcmUgZXNwZWNpYWxseSBjb25jZXJuZWQgYWJvdXQgdGhlaXIgaW1wYWN0IG9uIHN0dWRlbnRz4oCZIHNraWxsIGRldmVsb3BtZW50LCB0aG91Z2ggbWFueSByZW1haW4gb3B0aW1pc3RpYyB0aGF0IExMTXMgd2lsbCB1bHRpbWF0ZWx5IGJlIGEgdXNlZnVsIHRvb2wgdG8gaGVscCBzdHVkZW50cyBpbXByb3ZlIHRoZWlyIHdyaXRpbmcgc2tpbGxzLiJ9XX1d' # @param {isTemplate: true}
generation_config_b64 = 'eyJ0ZW1wZXJhdHVyZSI6MC45LCJ0b3BfcCI6MSwidG9wX2siOjEsIm1heF9vdXRwdXRfdG9rZW5zIjoyMDQ4LCJzdG9wX3NlcXVlbmNlcyI6W119' # @param {isTemplate: true}
safety_settings_b64 = 'W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d' # @param {isTemplate: true}

contents = json.loads(base64.b64decode(contents_b64))
generation_config = json.loads(base64.b64decode(generation_config_b64))
safety_settings = json.loads(base64.b64decode(safety_settings_b64))

stream = False

contents

generation_config

safety_settings

"""### Load image data from Drive-IDs"""

"""### Call the API"""

# Call the model and print the response.
gemini = genai.GenerativeModel(model_name=model)
contents="Analyze the provided news article write date,number of words, number of spaces, wordcloud and identify the key themes and underlying motivations of the individuals involved in six lines."
response = gemini.generate_content(
    contents,
    generation_config=generation_config,
    safety_settings=safety_settings,
    stream=False)

# Call the API
gemini = genai.GenerativeModel(model_name=model)
response = gemini.generate_content(contents, generation_config=generation_config, safety_settings=safety_settings, stream=False)

# Display output
st.title("Generated Output")
display_output(contents, response)
if generation_config.get('candidate_count', 1) == 1:
  display(Markdown(response.text))
else:
  print(response.candidates)

response.candidates

response.prompt_feedback

