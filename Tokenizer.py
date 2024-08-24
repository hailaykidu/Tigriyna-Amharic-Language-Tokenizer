#Tokenizer
#Amazing Result for Tigriyna Tokenizer 
import re

def tokenize_tigriyna(text):
    # Define regular expressions for tokenization
    word_pattern = r'\b\w+\b'  # Match alphanumeric words
    punctuation_pattern = r'[^\w\s]'  # Match punctuation marks

    # Tigriyna stopwords and punctuation
    tigrinya_stopwords = [
        "'ምበር", "'ሞ", "'ቲ", "'ታ", "'ኳ", "'ውን", "'ዚ", "'የ", "'ዩ", "'ያ", "'ዮም", "'ዮን",
        "ልዕሊ", "ሒዙ", "ሒዛ", "ሕጂ", "መበል", "መን", "መንጎ", "መጠን", "ማለት", "ምስ", "ዝኾነ", "ዝዀነ",
        "የለን", "ይቕረብ", "ይብል", "ይኸውን", "ይኹን", "ይኽእል", "ደኣ", "ድሕሪ", "ድማ", "ገለ", "ገሊጹ",
        "ገና", "ገይሩ", "ግና", "ግን", "ጥራይ", "ምባል", "ምእንቲ", "ምኽንያቱ", "ምኽንያት", "ምዃኑ",
        "ምዃንና", "ምዃኖም", "ስለ", "ስለዚ", "ስለዝበላ", "ሽዑ", "ቅድሚ", "በለ", "በቲ", "በዚ", "ብምባል",
        "ብተወሳኺ", "ብኸመይ", "ብዘይ", "ብዘይካ", "ብዙሕ", "ብዛዕባ", "ብፍላይ", "ተባሂሉ", "ነበረ", "ነቲ",
        "ነታ", "ነቶም", "ነዚ", "ነይሩ", "ነገራት", "ነገር", "ናብ", "ናብቲ", "ናትኩም", "ናትኪ", "ናትካ",
        "ናትክን", "ናይ", "ናይቲ", "ንሕና", "ንሱ", "ንሳ", "ንሳቶም", "ንስኺ", "ንስኻ", "ንስኻትኩም", "ንስኻትክን",
        "ንዓይ", "ኢለ", "ኢሉ", "ኢላ", "ኢልካ", "ኢሎም", "ኢና", "ኢኻ", "ኢዩ", "ኣለኹ", "ኣለዉ", "ኣለዎ",
        "ኣላ", "ኣሎ", "ኣብ", "ኣብቲ", "ኣብታ", "ኣብኡ", "ኣብዚ", "ኣነ", "ኣዝዩ", "ኣይኮነን", "ኣይኰነን",
        "እምበር", "እሞ", "እተን", "እቲ", "እታ", "እቶም", "እንተ", "እንተሎ", "እንተኾነ", "እንታይ", "እንከሎ",
        "እኳ", "እዋን", "እውን", "እዚ", "እዛ", "እዞም", "እየ", "እየን", "እዩ", "እያ", "እዮም", "ከሎ",
        "ከመይ", "ከም", "ከምቲ", "ከምኡ", "ከምዘሎ"
    ]
    tigriyna_punctuation = ['፣', '።', '፤', '!', '?']  # Add more punctuation marks as needed

    # Tokenize the text
    tokens = []
    for match in re.finditer(word_pattern, text):
        word = match.group(0)
        if word not in tigrinya_stopwords: 
            tokens.append(word)
    for match in re.finditer(punctuation_pattern, text):
        punctuation = match.group(0)
        if punctuation not in tigriyna_punctuation:
            tokens.append(punctuation)
    return tokens

def count_code_statistics(tokens):
    num_lines = len(tokens)
    num_characters = sum(len(token) for token in tokens)
    num_tokens = len(tokens)
    return num_lines, num_characters, num_tokens

def main():
    # Read the dataset
    with open("/home/hailay/Desktop/EXLM_R/multilingual_train.tsv", "r", encoding="utf-8") as file:
        tigriyna_text = file.read()

    # Tokenize the text
    tokens = tokenize_tigriyna(tigriyna_text)

    # Save the tokenized output to a file
    with open("/home/hailay/Desktop/EXLM_R/tigriyna_text", "w", encoding="utf-8") as file:
        file.write(" ".join(tokens))

    # Calculate code statistics
    num_lines, num_characters, num_tokens = count_code_statistics(tokens)
    print("Code Statistics:")
    print(f"Number of lines: {num_lines}")
    print(f"Number of characters: {num_characters}")
    print(f"Number of tokens: {num_tokens}")

if __name__ == "__main__":
    main()
