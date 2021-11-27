from flask import Flask
from flask import render_template
import sqlite3 

con = sqlite3.connect('store.db')

con.execute('CREATE TABLE users(Username VARCHAR(255) , Password VARCHAR(255))')
con.close() 

'''con.execute('CREATE TABLE books(id VARCHAR(255) PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), description VARCHAR(255),image TEXT, price DOUBLE)')
con.close()  


con = sqlite3.connect('store.db')
con.execute('INSERT INTO books(id, title, author, description, image, price) VALUES (9780241466940, "The Fortune Men: Shortlisted for the Booker Prize 2021", "Nadifa Mohamed", "Chilling and utterly compelling , The Fortune Men shines an essential light on a much-neglected period of our national life Sathnam Sanghera","product-images/The Fortune Men.jpg", 12.50),(9781910688922, "An Island", "Karen Jennings ","An Island concerns itself with lives lived on the margins, through the story of a man who has exiled himself from the known world only to find himself called to the service of others", "product-images/An Island.jpg", 10.00),(9781787333345, "Silent Earth: Averting the Insect Apocalypse", "Dave Goul","We have to learn to live as part of nature, not apart from it. And the first step is to start looking after the insects, the little creatures that make our shared world go round. Insects are essential for life as we know it", "product-images/Silent Earth.jpg", 15.25),(9781847924018, "Four Thousand Weeks: Embrace your limits. Change your life.", "Oliver Burkeman ","We are obsessed with our lengthening to-do lists, our overfilled inboxes, the struggle against distraction, and the sense that our attention spans are shrivelling. Still, we rarely make the connection between our daily struggles with time and the ultimate time management problem: the question of how best to use our ridiculously brief time on the planet, which amounts on average to about four thousand weeks", "product-images/Four Thousand Weeks.jpg", 15.79),(9780241381861, "Connections: A Story of Human Feeling", "Karl Deisseroth","In this riveting journey through the hidden realms of the human mind, a world-renowned psychiatrist and neuroscientist explores the origins of human emotion, and examines what mental illnesses reveal about all of us ", "product-images/Connections.jpg", 18.60),(9780571368983, "Why Solange Matters", "Stephanie Phillips ","The dramatic story of Solange: a musician and artist whose unconventional journey to international success was far more important than her family name.", "product-images/Why Solange Matters.jpg", 9.29),(9780241243213, "Antwerp: The Glory Years", "Michael Pye","A rich history of Antwerp from the author of the acclaimed bestseller The Edge of the World Even before Amsterdam there was a dazzling North Sea port at the hub of the city of Antwerp.", "product-images/Antwerp.jpg", 23.25),(9781846148248, "The World According to Colour: A Cultural History", "James Fox ","A beguiling cultural history of colour by the BAFTA nominated broadcaster and art historian James Fox", "product-images/The World According to Colour.jpg", 23.25),(9781529388626, "Earthshot: How to Save Our Planet", "Colin Butfield","The Earthshot concept is simple: Urgency + Optimism = Action . We have ten years to turn the tide on the environmental crisis, but we need the worlds best solutions and one shared goal - to save our planet.", "product-images/Earthshot.jpg", 18.60),(9781787417663, "Art of Protest: What a Revolution Looks Like", "De Nichols ","From the psychedelic typography used in Make Love Not War posters of the 60s, to the solitary raised fist, take a long, hard look at some of the most memorable and striking", "product-images/Art of Protest.jpg", 15.79);')
            
con.commit()
'''
con.close()  







