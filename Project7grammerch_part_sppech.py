import streamlit as st
from language_tool_python import LanguageTool

def grammar_check(text):
    tool = LanguageTool('en-US')
    matches = tool.check(text)
    return matches
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Function to perform part-of-speech tagging on input text
def tag_text(input_text):
    # Tokenize input text into words
    words = word_tokenize(input_text)
    
    # Perform part-of-speech tagging on the tokenized words
    tagged_words = pos_tag(words)
    
    return tagged_words
def main():
    # st.title("Streamlit App with Slider Navigation")

    # Add a slider widget to select a project
    selected_project = st.sidebar.radio("Navigation", ["Grammar Checking App", "Part-of-Speech Tagging App"])
    st.sidebar.write('Project 1: Grammar Checking App')
    st.sidebar.write('Project 2: Part-of-Speech Tagging App')
    # st.sidebar.write('Project 3: Language Translation To French')
    # Display content based on the selected project
    if selected_project =="Grammar Checking App" :
        st.write("Project 1: Grammar Checking App")
        # Load sentiment analysis pipeline
        st.title("Grammar Checking App")

        text_input = st.text_area("Enter text to check for grammar errors:")
        if st.button("Check Grammar"):
            if text_input:
                matches = grammar_check(text_input)
                if matches:
                    st.write("Grammar errors found:")
                    for match in matches:
                        # Check if msg attribute exists
                        msg = match.msg if hasattr(match, 'msg') else None
                        # Check if fromx and tox attributes exist
                        fromx = match.fromx if hasattr(match, 'fromx') else None
                        tox = match.tox if hasattr(match, 'tox') else None
                        # Check if replacements attribute exists
                        replacements = match.replacements if hasattr(match, 'replacements') else None
                        st.write(f"{match.ruleId}: {msg} ({fromx} - {tox}): {replacements}")
                else:
                    st.write("No grammar errors found.")
            else:
      
                st.write("Please enter some text to check.")
    if selected_project =="Part-of-Speech Tagging App" :
        st.write("Project 2: Part-of-Speech Tagging App")
        # Load sentiment analysis pipeline
        # st.title("Grammar Checking App")


# import streamlit as st


    # Streamlit app
        st.title("Part-of-Speech Tagging App")
        
        # Text input for user input
        input_text = st.text_area("Enter some text:", height=200)
        
        # Perform tagging when the user submits the input
        if st.button("Tag Text"):
            # Perform part-of-speech tagging on the input text
            tagged_text = tag_text(input_text)
            
            # Display tagged text
            st.subheader("Tagged Words:")
            for word, tag in tagged_text:
                st.write(f"{word}: {tag}")

if __name__ == "__main__":
    main()
