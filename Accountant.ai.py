import spacy

# Load the pre-trained model
nlp = spacy.load("en_core_web_lg")

# Define the words to compare
words = [
"Discount Allowed (Before GST)",
"Food Sale (GST @5%)",
"Liquor Sales (Vat 22%)",
"Soft Beverages Sales (GST 5%)",
"Swiggy & Zomato Sales",
"Coconuts",
"Vegetables & Fruits",
"French Fries",
"Groceries/spices",
"Baskin Robins Icecream",
"Icecream( Local)",
"Liquor Items",
]

# Calculate the similarity matrix
similarity_matrix = [[nlp(word1).similarity(nlp(word2)) for word2 in words] for word1 in words]

# Print the similarity matrix
for row in similarity_matrix:
    print(row)

# Set a similarity threshold
similarity_threshold = 0.5

# Group similar words
groups = []
for i, word1 in enumerate(words):
    for j, word2 in enumerate(words):
        if i != j and similarity_matrix[i][j] > similarity_threshold:
            # Check if the words are already in a group
            word1_group = None
            word2_group = None
            for group in groups:
                if word1 in group:
                    word1_group = group
                if word2 in group:
                    word2_group = group

            # Add the words to the same group or create a new group
            if word1_group and word2_group:
                if word1_group != word2_group:
                    word1_group.extend(word2_group)
                    groups.remove(word2_group)
            elif word1_group:
                word1_group.append(word2)
            elif word2_group:
                word2_group.append(word1)
            else:
                groups.append([word1, word2])

print("Groups:", groups)
