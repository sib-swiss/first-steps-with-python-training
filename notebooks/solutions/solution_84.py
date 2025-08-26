code_languages = {
    'Java': 17.2, 
    'Python': 22.2, 
    'PHP': 8.8,
    'JavaScript':8, 
    'R':9.3, 
    'C++': 6.7
}

plt.bar(code_languages.keys(), code_languages.values(), color='green')
plt.ylabel('Popularity')
plt.show()

