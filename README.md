Hello :>

All you need is the app folder, everything else is unnecessary for this to work. Make sure that you have a valid groq api key and edit the .env file so that it contains your key. Do not add "" around it.

The user inputs a cuisine type (e.g. Mexican, Italian) in which the llm then takes that cuisine and generates a supposedly unique restaurant name and a matching 3-course meal menu for the restaurant. 
Note: Due to the temperature being set to 0.7, rerunning the application can lead to slight different results every time. You can change this setting in llm.py.

For it to work, in the command prompt type: streamlit run <path to main.py>. If for whatever reason command prompt doesn't allow streamlit commands, use: python -m streamlit run <path to main.py>.