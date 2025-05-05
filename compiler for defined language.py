
import tkinter as tk
from tkinter import filedialog


# Function to open a file and display its content in the "Input" text box
def open_file():
  file_path = filedialog.askopenfilename()
  if file_path:
    with open(file_path, 'r') as file:  # Open the selected file in read mode
      content = file.read()  # Read the content of the file
      input_text.delete(1.0, tk.END)  # Clear the input text box
      input_text.insert(tk.END,
                        content)  # Insert the content into the input text box


# Function to save the content of the "Output" text box to a text file
def save_file():
  file_path = filedialog.asksaveasfilename(
      defaultextension=".txt")  # Open the file dialog for saving
  if file_path:
    content = output_text.get(1.0,
                              tk.END)  # Get the content of the output text box
    with open(file_path, 'w') as file:  # Open the file in write mode
      file.write(content)  # Write the content to the file


# Function to remove text from both the "Input" and "Output" text boxes
def remove_text():
  input_text.delete(1.0, tk.END)  # Clear the content of the input text box
  output_text.delete(1.0, tk.END)  # Clear the content of the output text box


def length(word):
  counter = 0  # Initialize a counter variable to keep track of the number of characters

  # Iterate through each character in the input word
  for char in word:
    counter += 1  # Increment the counter for each character in the word

  return counter  # Return the final count, representing the length of the word
def removing_spaces_comments(input_text):
 
  processed_text = input_text
  input_text = ''
  space = " "
  counter_commet = 1
  temp_part = ''
  previous_was_space = False
  previous_was_newline = False

  for char in processed_text:
      if counter_commet == 1:
          if char != '%' and char != ' ' and char != '\n':
              input_text += char
              previous_was_space = False
              previous_was_newline = False
          elif char == '%' or char == ' ' or char == '\n':
              if char == '%':
                  counter_commet *= -1  # Toggle between the two modes
              else:
                  if not previous_was_space and not previous_was_newline:
                      input_text += space
                  previous_was_space = True if char == ' ' else False
                  previous_was_newline = True if char == '\n' else False
      else:
          if char != '%' and char != ' ' and char != '\n':
              input_text += ''
              previous_was_space = False
              previous_was_newline = False
          elif char == '%' or char == ' ' or char == '\n':
              if char == '%':
                  counter_commet *= -1  # Toggle between the two modes
              else:
                  if not previous_was_space and not previous_was_newline:
                      input_text += space
                  previous_was_space = True if char == ' ' else False
                  previous_was_newline = True if char == '\n' else False

  return input_text




def separation_text(txt):
  text_processed = txt
  txt = ""
  output=""
  # Define separators to separate different components in the text
  separator = set('+-*/=(){}[]<>,;.')
  # Define operators that need special handling
  operations = set('+-*/=')
  # Define numeric characters
  number = set('0123456789')
  # Define alphabetic characters
  alpha = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
  signals = set('+-')
  alphanumeric = alpha | number
  equality = set('<>!=:')
  punctuation = set(';,')
  buffer=''

  if length(text_processed) >= 1:
     text_processed = text_processed + "#"

  i = 0
  while i < length(text_processed):
      #if buffer.lower() in ['BEGIN', 'FIN.', 'PROGRAMME', 'INT', 'REAL', 'CHAR', 'STRING', 'OR', 'AND', 'IF', 'ELSE',
         #'BOOLEAN', 'FOR', 'WHILE', 'DO', 'WHEN']:
         # txt += buffer.lower() +'#'
        #  buffer=''
      
      if i == length(text_processed) - 1:
          break
      elif text_processed[i]==' ':
        i+=1
      if text_processed[i]in alphanumeric and text_processed[i + 1]in alphanumeric or text_processed[i + 1] == '_' \
          or text_processed[i] == '_' and text_processed[i + 1] in alphanumeric \
          or i == 0 and text_processed[i] in signals and text_processed[i + 1] in number \
          or text_processed[i] in signals and text_processed[i + 1] == '.' and text_processed[i + 2] in number and i == 0 \
          or text_processed[i] in equality and text_processed[i + 1] == '=' \
          or text_processed[i - 1] in equality and text_processed[i] == '=' and text_processed[i + 1] == '=' and not text_processed[i + 2] in number and not text_processed[i + 2] == '.' \
          or text_processed[i] in number and text_processed[i + 1] == '.' \
          or text_processed[i] == '.' and text_processed[i + 1] in number  \
          or text_processed[i - 1] in operations and text_processed[i] in signals and text_processed[i + 1] in number \
          or text_processed[i - 1] in alphanumeric and text_processed[i] == '+' and text_processed[i + 1] == '+' and not text_processed[i + 2] in number and not text_processed[i + 2] == '.' \
          or text_processed[i - 1] in alphanumeric and text_processed[i] == '-' and text_processed[i + 1] == '-' and not text_processed[i + 2] in number and not text_processed[i + 2] == '.' \
          or text_processed[i - 1] in punctuation and text_processed[i] in signals and text_processed[i + 1] in number\
          or text_processed[i - 1] in operations and text_processed[i] in signals and text_processed[i + 1] == '.' \
          or text_processed[i - 1] in signals  and text_processed[i] in signals  and text_processed[i + 1] == '.' \
          or text_processed[i - 1] == '=' and text_processed[i] in signals and text_processed[i + 1] == '.':
          txt += text_processed[i]
      
      elif i == i and text_processed[i - 1] in signals and text_processed[i] in signals and text_processed[i + 1] in number:
          txt += "#" + text_processed[i]
      elif text_processed[i]=='#':
          txt += text_processed[i]
      else:
          txt += text_processed[i] + "#"
      i += 1
  # Remove trailing '#' characters
  while txt[-1] == '#':
     txt= txt[:-1]
  txt += "#"
  i=0
 

  #Add '#' to the end

  return txt


def type_transition(carecter):
  # Define sets of characters for different types
  number = set('0123456789')
  alpha = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
  punctuation = set(';.()')
  operation=set('*/')

  # Check the type of the input character and return a corresponding code
  if carecter in number:  # If the character is a digit
    return 0
  elif carecter == '+':  # If the character is '+'
    return 1
  elif carecter == '-':  # If the character is '-'
    return 2
  elif carecter == '=':  # If the character is '='
    return 3
  elif carecter == '.':  # If the character is '.'
    return 4
  elif carecter == '_':  # If the character is '_'
    return 5
  elif carecter == '<' or carecter == '>':  # If the character is '<' or '>'
    return 6
  elif carecter in punctuation:  # If the character is '(', ')', ';', or '.'
    return 7
  elif carecter in operation:  # If the character is '*' or '/'
    return 8
  elif carecter == ':':  # If the character is ':'
    return 9
  elif carecter in alpha:  # If the character is an alphabetic character
    return 10
  elif carecter == '!':  # If the character is '!'
    return 11
  else:
    return -1  # Return -1 for characters that don't match any type
def Key(word):
  word_no_space = ""
  for char in word:
      if char != " ":
          word_no_space += char

  if word_no_space == "BEGIN" or word_no_space == "END" or word_no_space == "PROGRAMME" or word_no_space == "INT" or \
          word_no_space == "REAL" or word_no_space == "CHAR" or word_no_space == "STRING" or word_no_space == "OR" or \
          word_no_space == "AND" or word_no_space == "IF" or word_no_space == "ELSE" or word_no_space == "BOOLEAN" or \
          word_no_space == "FIN." or word_no_space == "DO" or word_no_space == "EXECUTE" or word_no_space == "VAR" or \
          word_no_space == "FOR" or word_no_space == "OTHERWISE" or word_no_space == "CONST" or word_no_space == "IDF"\
         or word_no_space =="WHILE":
      return True
  return False
def carecter_majuscule(carecter):
  if carecter >= 'A' and carecter <= 'Z':
      return True
  return False
def type_entite(Ec, input):
  i = ''
  entite = ''
  for char in input:
    if char != ' ':
      entite += char
  if Ec == 1:
    if length(entite) < 7  :
        if carecter_majuscule(entite):
            if(Key(entite)):
              i += " " + entite + ":entite correct est un identifier \n"
            else:
              i += " " + entite+ ":entite incorrect\n "
        else:
             i += " " + entite + ":entite correct est un identifier \n"
    else:
            i += " " + entite + ":entite incorrect\n "
  elif Ec == 4:
    try:
      if length(entite) < 8 and int(entite) < 1333635:
        i += " " + entite + ": entite est un constante \n"
      else:
        i += " " + entite + ":entite incorrect\n "
    except ValueError:
      i += " " + entite + ":entite incorrect\n "
  elif Ec == 5:
    i += " " + entite + ":entite est un opérateur - \n"
  elif Ec == 6:
    i += " " + entite + ":entite est un opérateur + \n"
  elif Ec == 7:
    if length(entite) < 10 :
        i += " " + entite + ":entite est un nombre real \n"
    else:
        i += " " + entite + ":entite incorrect\n "
  elif Ec == 8:
    if length(entite) < 10 :
        i += " " + entite + ":entite est un nombre real \n"
    else:
        i += " " + entite + ":entite incorrect\n "
  elif Ec == 12:
    i += " " + entite + ":entite est un opérateur + \n"
  elif Ec == 13:
    i += " " + entite + ":entite est un séparateur  \n"
  elif Ec == 14:
    i += " " + entite + ":entite est un opérateur \n"
  elif Ec == 15:
    i += " " + entite + ":entite est un opérateur \n"
  elif Ec == 16:
    i += " " + entite + ":entite est un séparateur  \n"
  elif Ec == 17:
    i += " " + entite + ":entite est un opérateur - \n"
  elif Ec == 18:
    i += " " + entite + ":entite est un séparateur  \n"
  else:
    i += " " + entite + ":entite incorrect\n "
  output_text.insert(tk.END, i + "\n")


def automate():
  #0,#1,#2,#3,#4,#5,#6,#7,#8,#9,#10,#11,#12
  matrice = [
      [4, 6, 5, 13, 9, -1, 13, 16, 15, 18, 1, -1],  # 0
      [1, -1, -1, -1, -1, 2, -1, -1, -1, -1, 1, -1],  # 1
      [1, -1, -1, -1, -1, 3, -1, -1, -1, -1, 1, -1],  # 2
      [-1, -1, -1, -1, -1, 2, -1, -1, -1, -1, -1, -1],  # 3
      [4, -1, -1, -1, 7, -1, -1, -1, -1, -1, -1, -1],  # 4
      [4, -1, 17, -1, 9, -1, -1, -1, -1, -1, -1, -1],  # 5
      [4, 12, -1, -1, 9, -1, -1, -1, -1, -1, -1, -1],  # 6
      [8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 7
      [8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 8
      [8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 9
      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 10
      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 11
      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 12
      [-1, -1, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1],  # 13
      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 14
      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 15
      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 16
      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 17
      [-1, -1, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1],  # 18
  ]
  seperator_text = process_input_return()
  indice = 0
  ts = ''
  Ec = 0
  for indice in range(length(seperator_text)):
    print(Ec)
    tc = seperator_text[indice]
    if tc != '#':
      ts = ts + seperator_text[indice]
      if Ec != -1 and type_transition(tc) != -1:
        Ec = matrice[Ec][type_transition(tc)]
      # else :ec=-1
    else:
      type_entite(Ec, ts)
      ts = ''
      Ec = 0


def process_input_return():
  text = input_text.get("1.0",
                        "end-1c")  # Get the content of the input text box
  processed_text = removing_spaces_comments(text)
  processed_text = separation_text(processed_text)
  return processed_text


def process_input_affichage():
  text = input_text.get("1.0",
                        "end-1c")  # Get the content of the input text box
  processed_text = removing_spaces_comments(text)
  processed_text = separation_text(processed_text)
  output_text.insert(tk.END, processed_text + "\n")


def output():
  output_text.delete("1.0", "end")
  process_input_affichage()
  automate()


# Create the main application window
root = tk.Tk()  # Create the main window
root.title("Interface")  # Set the title of the window

menu = tk.Menu(root)  # Create a menu for the window
root.config(menu=menu)  # Configure the menu for the window

file_menu = tk.Menu(menu)  # Create a submenu for file-related options
menu.add_cascade(label="File",
                 menu=file_menu)  # Add the submenu to the main menu
file_menu.add_command(label="Open",
                      command=open_file)  # Add an option to open a file
file_menu.add_command(
    label="Save",
    command=save_file)  # Add an option to save the output to a file
file_menu.add_command(label="Remove",
                      command=remove_text)  # Add an option to remove text
file_menu.add_separator()  # Add a separator in the menu
file_menu.add_command(label="Exit",
                      command=root.quit)  # Add an option to exit the program

input_label = tk.Label(root,
                       text="Input:")  # Create a label for the input text box
input_label.pack()  # Display the input label

input_text = tk.Text(root, height=20, width=50)  # Create the input text box
input_text.pack()  # Display the input text box

output_label = tk.Label(
    root, text="Output:")  # Create a label for the output text box
output_label.pack()  # Display the output label

output_text = tk.Text(root, height=20, width=50)  # Create the output text box
output_text.pack()  # Display the output text box

process_input_button = tk.Button(
    root, text="OK", command=output)  # Create a button to process the input
process_input_button.pack()  # Display the process input button

root.mainloop()  # Start the main event loop for the application
