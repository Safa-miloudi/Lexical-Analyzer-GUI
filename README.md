# Compilation Module Project - Lexical Analyzer GUI  

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)  
![License](https://img.shields.io/badge/License-MIT-green)  

**Academic Project** | Semester 5 | 3rd Year - Compilation Techniques Course  
---

## 🔍 Overview  
GUI application implementing lexical analysis phases for a custom language, featuring:  
- Comment/whitespace preprocessing  
- Token separation engine  
- 18-state finite automaton  
- Token classification system  
- Error detection mechanisms

  ---
## 🧩 Features

### ✅ GUI Functionalities
- **Open File:** Load code from a text file into the input area.
- **Save File:** Save the output (processed code) to a file.
- **Clear Text:** Clears both the input and output windows.
- **Process Code:** Clean and tokenize the input code.

### 🔍 Preprocessing Capabilities
- **Comment Removal:** Deletes comments between `%...%`.
- **Whitespace Normalization:** Cleans extra spaces and newlines.
- **Lexical Separation:** Separates tokens such as keywords, operators, and delimiters.
- **Custom Token Rules:** Detects compound operators like `++`, `--`, `==`, etc.

---

## 🖼️ GUI Layout

The interface is built with **Tkinter** and includes:
- A text box for code input (left side)
- A text box for output (right side)
- Action buttons (top): Open, Save, Clear

---

## 🧠 How It Works

1. Load or write your code in the left input area.
2. Click **"Save File"** to tokenize and save the processed code.
3. Comments wrapped in `%...%` will be removed.
4. Symbols and keywords are separated and cleaned.
   
---
## 📝 Authors
- Safa Miloudi
  
## 📚 More Information  
**Course:** Compilation Techniques (S5 - 3rd Year) (Kasdi Merbah Ouargla University, 2023/2024)  
**Concepts Demonstrated:**  
- Finite automata design  
- Lexical error handling  
- Token pattern matching  
- Symbol table foundations
For more details, see the [Report](https://mega.nz/file/MipwWTgY#gBuDmEpJANLdfEpU6G4ugajnSWWsZOzVkN1veUgI17g).



---
