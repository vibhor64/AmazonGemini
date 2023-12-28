# import bardapi
import streamlit as st
import main
import google.generativeai as genai

# Set up your OpenAI API credentials
# token = "dQgXUuYI8k6yct8ovVUjv3vCAJQqaDUZp0XDUDu9U2ZA_iyFMU2WUgPHczdpZ5CBnovCrg."

# spid_value = "dQgXUuYI8k6yct8ovVUjv3vCAJQqaDUZp0XDUDu9U2ZA_iyFMU2WUgPHczdpZ5CBnovCrg."
# token = "SNlM0e={}".format(spid_value)  

GOOGLE_API_KEY='AIzaSyDbQus67GYsqO6k10dlif8wwoGgdIw2X54'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

st.title("Product Review Summarizer")
review = st.text_area("Enter the link:")


if st.button("Summarize"):
        if review:
            item_name, rating_list, review_text = main.amazonScrape(review)
            if not review_text: 
                print('No reviews found, our product rating might not be accurate...')
                st.error('No reviews found, our product rating might not be accurate...')
                item_name = str(item_name)
                prompt = str("I found this item on amazon named" + item_name + "Summarize this product based off its ratings and product description within 30 lines and generate a table containing pros and cons of this product, and also give a score out of 10 whether one should buy this product or not")
                print("Waiting for Gemini ⏳")
                # response = bardapi.core.Bard(token).get_answer(prompt)
                response = model.generate_content(prompt)
                response = response.text
                print(response)
                st.write(response)
                print("Target response received! 🎉")
            else:
                rating_str = ", ".join(str(rating) for rating in rating_list)
                review_str = ",".join(str(review) for review in review_text)
                # review_str = str(review_str)
                # rating_str = str(rating_list)
                item_name = str(item_name)
                prompt = str("I found this item on amazon named " + item_name + "Summarize these amazon reviews based off its product ratings, description on its webpage, within 30 lines and generate a table containing pros and cons of this product"+"The reviews are: " + review_str + "and their respective ratings are:"+ rating_str + "and also give a score out of 10 whether one should buy this product or not")           
                # user_input = input(prompt)

                response = model.generate_content(prompt)
                response = response.text
                print(response)
                st.write(response)
                print("Target response received! 🎉")
        else:
            st.warning("Please provide a valid link")
            


# streamlit run c:\Users\vibho\Documents\Coding\Python\amazonScrape\app.py
