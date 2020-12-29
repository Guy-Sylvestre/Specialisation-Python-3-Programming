stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"


Ecrire un code qui utilise la chaîne de caractères stockée dans send et crée un acronyme qui est attribué à la variable acro. Les deux premières lettres de chaque mot doivent être utilisées, chaque lettre de l'acronyme doit être en majuscule et chaque élément de l'acronyme doit être séparé par un "..." (point et espace). Les mots qui ne doivent pas être inclus dans l'acronyme sont stockés dans la liste des mots vides. Par exemple, si la chaîne "height and ewok wonder" a été attribuée à send, l'acronyme résultant devrait être "HE. EW. WO".

Traduit avec www.DeepL.com/Translator (version gratuite)*


#######################################################################################


p_phrase = "was it a car or a cat I saw"

Un palindrome est une phrase qui, si elle était inversée, se lirait exactement de la même façon. Écrivez un code qui vérifie si p_phrase est un palindrome en l'inversant et en vérifiant ensuite si la version inversée est égale à l'original. Assignez la version inversée de p_phrase à la variable r_phrase afin que nous puissions vérifier votre travail.


#######################################################################################
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]


Il s'agit d'une liste de données sur l'inventaire d'un magasin où chaque article de la liste représente le nom d'un article, la quantité en stock et son coût. Imprimez chaque article de la liste avec le même formatage, en utilisant la méthode .format (pas de concaténation de chaînes). Par exemple, la première déclaration d'impression devrait être la suivante Le magasin a 12 chaussures, chacune au prix de 29,99 USD.