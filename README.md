# Cafe-House
Cafe House website

  # Café House
A website where customer can order food items quickly or can see a meal which is changing day by day.
1.	Idea:
If a client is planning to open a brand-new restaurant in a city then he can use this website because this website is pretty straight forward where you just need to login and place the order. 
2.	About Project:

How a new user will use it?

-> If you are a new user then you don’t need to login if your intention is to just go through our restaurant menu or want to checkout prices of the items. No authentication or authorization is required for this process.
-> If you are willing to order some items which you have selected, then you need to have an account. If you are a regular customer then you have an account so just login and place the order immediately. But if you are a new user then you need to have an account so just follow the link and then create a new one.
-> If you have any query or suggestions or you want to contact to the owner for a mass order or delivery then just go to the Contact field and communicate to the owner easily. Owner will contact you or reply you within a minute. 
-> You can go through the restaurant map there which have the exact location of restaurant if you are willing to eat at the restaurant.

Different sections in the project 
 
1. Home 
    -> Introduction section: On this page you will have a small introduction about restaurant and the history related to this restaurant.
   -> Popular Item section: Here you will see a popular item section which is basically decided by the reviews of the customer (I haven’t implemented more about this). Items having more reviews will be listed in this list. Based on the reviews we will decide a popularity index and we just sort the items based on that in descending order. Items having greater values of popularity index will have more popularity. I am trying to add one more functionality where popularity index will also be affected by how many times an item has been ordered or based on the order frequency of an item.
   -> Daily menu section: This section will have daily menu items. Though some items are much popular so they will be made specially on some special days of the week. This can be decided by any algorithm. In this project I have created that there will be 7 items which will be made 7 days of the week specially.

2. Today Special:
-> This section will have information about today’s special item. How it will be decided? Though I have taken a simple algorithm where the item will be changed by the days of the week. During the insertion of the particular item, we’ll take “Day” as an input. So, we’ll just take the current day e.g. 0 – Sunday ,1-Monday etc. So, we’ll just take the day %7. So, items will change automatically. We don’t need to change this manually every day.

3. Menu: 
   ->This section will have menu about all items available in the restaurant. We can further classify this section in many small subsections though, based on the characteristics of the food or based on popularity index or may be based on the origin of the particular item. Any algorithm can be use here. I just used a simple one and popped all items and showed them on the front end.  

4. Contact 
-> This section has a short message form where a customer can review about a food or can send any small service requirements messages etc. A user can contact to the owner through this section. All the contact related information will be pasted here.
-> This section consists a small google map. Which I have developed via google map API through java script. We can change this where admin can put coordinates of the location of the restaurant. This change can only be done by the admin or owner of the restaurant.

5.Admin:
->This page will only be accessed by the owner of this restaurant.
->Through this page an owner can update all the information about this restaurant. 
-> This page has 
         -> Update restaurant info or edit welcome note	 
         -> Add a new item in the menu 
        -> Update an existing item 
        -> This page will show the current sent messages through contact form
        -> This page will also track the newly registered user’s information 
                        6. Login / logout 
                             -> Via this section a user can be authenticated easily.
  3. Used tools and technologies 
  Backend: Django, Python
  Front end: HTML5, CSS3, BOOTSTRAP, Google Map API, Java script 
 Data base: SQL Database, Django Database Administration
 Hosting: Pythonanywhere.com which is a free web hosting service provider 
 Ide: PyCharm 
                   4.Future Scope:
                  -> This project can be further modified based on the requirements. Some of them are:
                       1. Add a live tracker which can track your order 
                       2. One to one chat system can be added for better interaction
                       3. Modified login/register form fields 
                       4. Can be added some better payment security methods
                       5. Better review system
             

 



# Live Website Link
# https://cafehouse.pythonanywhere.com/
