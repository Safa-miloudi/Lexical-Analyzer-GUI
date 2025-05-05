# Compilation Module Project - Lexical Analyzer GUI  

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)  
![License](https://img.shields.io/badge/License-MIT-green)  

**Academic Project** | Semester 5 | 3rd Year - Compilation Techniques Course  

<img src="https://raw.githubusercontent.com/yourusername/reponame/main/screenshot.png" width=600 alt="GUI Screenshot">  

## 🔍 Overview  
GUI application implementing lexical analysis phases for a custom language, featuring:  
- Comment/whitespace preprocessing  
- Token separation engine  
- 18-state finite automaton  
- Token classification system  
- Error detection mechanisms  

## 🎯 Key Features  
| Component | Implementation |  
|-----------|----------------|  
| **GUI Interface** | Dual-pane text editor with file operations |  
| **Preprocessor** | `removing_spaces_comments()` - Removes %-style comments |  
| **Tokenizer** | `separation_text()` - Splits code into lexemes |  
| **State Machine** | `automate()` - 18x12 transition matrix implementation |  
| **Validator** | `Key()`, `type_entite()` - Checks keywords/constants |  

## 📚 Academic Context  
**Course:** Compilation Techniques (S5 - 3rd Year)  
**Concepts Demonstrated:**  
- Finite automata design  
- Lexical error handling  
- Token pattern matching  
- Symbol table foundations  

## 🛠️ Installation  
```bash
git clone https://github.com/yourusername/compilation-module-project.git
cd compilation-module-project
python compilation.py
