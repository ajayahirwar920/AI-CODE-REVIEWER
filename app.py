import streamlit as st # type: ignore

st.title ("AI-CODE-REVIEWER")

selected_lang = st.selectbox("Select the programming Language", ["Auto-detect","Python", "C", "JavaScript", "Java", "C++"]) ##!The selected language will be used for comparison 

#? Here the user can input the code they want to analyze. The code will be analyzed when the "Review Code" button is clicked.
code = st.text_area("Enter Your Code Here")
if(code == ""):
    if(st.button("Review Code")):
        st.error("❌ Please enter your code first before clicking the Review Code button.")
elif(code != ""):
    if(st.button("Review Code")):
        st.success("Code received successfully! ✅")
        
        from analyzer import analyze_code  #!Importing the analyze_code function
        from ai_reviewer import review_code
        detected_lang,confidence, syntax_result = analyze_code(code)
        
        if(selected_lang == "Auto-detect"):
            analysis_lang = detected_lang

        else:
            if detected_lang == "Ambiguous":
                st.warning("⚠️ Could not confidently detect the language.")
                st.write(f"We'll continue with the selected language {selected_lang} for analysis.")
                analysis_lang = selected_lang

            elif detected_lang == selected_lang:
                st.success("✅ Language verified.")
                analysis_lang = selected_lang

            else:
                st.warning(
                    f"⚠️ Language mismatch — Selected: {selected_lang}, "
                    f"Detected: {detected_lang}"
                )
                st.write(
                    f"The code analysis will continue using the detected language: {detected_lang}"
                )
                analysis_lang = detected_lang
                
        status = st.empty()
        status.write("Analyzing the code....")
        
        #! Gemini Call here
        review = review_code(code, analysis_lang)
        st.write(review)
        
        st.write("Detected Language: \n", detected_lang)
        st.write(f"Confidence: {confidence:.2f}%")
        if(syntax_result is not None):
            if syntax_result ["valid"]:
                st.success("Syntax : ✅ Valid")
            
            else:
                st.error("Syntax : ❌ Invalid")
                st.write("Error Message: \n", syntax_result["message"])
                st.write("Error Line: \n", syntax_result["line"])
                st.write("Error Column: \n", syntax_result["offset"])
        status.success("Analysis completed! ✅")
        
