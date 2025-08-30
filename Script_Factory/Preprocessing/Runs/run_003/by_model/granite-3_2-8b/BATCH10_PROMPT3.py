# BATCH10_PROMPT3_Granite.py

def create_hologram(text: str) -> None:
    """
    Creates a 'holographic' effect for the given input string by printing it in a circular pattern.

    Args:
    text (str): The string to be displayed as a hologram.

    Returns:
    None
    """
    # Clear console (Windows only, use sys.stdout.write("\033[H\033[J") for others)
    if 'win' in system().lower():
        _ = os.system('cls')  # For Windows
    else:
        _ = os.system('clear')  # For Unix/Linux/MacOS

    # Define the hologram pattern
    holo_pattern = """
                  {0}                
                 {0}{1}{0}             
                {0}{1}{2}{0}            
               {0}{1}{2}{3}{0}           
              {0}{1}{2}{3}{4}{0}          
             {0}{1}{2}{3}{4}{5}{0}         
            {0}{1}{2}{3}{4}{5}{6}{0}        
           {0}{1}{2}{3}{4}{5}{6}{7}{0}       
          {0}{1}{2}{3}{4}{5}{6}{7}{8}{0}      
         {0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{0}     
        {0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{a}{0}    
       {0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{ab}{0}     
      {0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{abc}{0}     
     {0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{abcd}{0}    
    {0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{abcde}{0}   
     """

    # Format the input text into hologram pattern
    formatted_text = holo_pattern.format(text[i] if i < len(text) else ' ' for i in range(len(text)))

    # Print the holographic effect
    print(formatted_text)


if __name__ == "__main__":
    text_input = input("Enter a string to create a hologram: ")
    create_hologram(text_input)