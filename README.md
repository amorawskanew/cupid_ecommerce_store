<img src='/media/ReadMe_image.jpg' style="margin: 0;">

Welcome amorawskanew,

<h2>Used Materials</h2>

1. Bootstrap 4 Cheat Sheet
https://hackerthemes.com/bootstrap-cheatsheet/
https://bootstrapcreative.com/resources/bootstrap-4-css-classes-index/

2. Footer-taken from bootstrap4 and modified
https://mdbootstrap.com/docs/standard/navigation/footer/

3. All the images were found on Google. I think I habve gone throught 50 to 60 various toy, chocolate, keyholders, flowers and pendants making companies.
    *Bears:  https://www.google.com/search?q=bears+love&sxsrf=ALeKk00FoCv0GiP7ycyTnlGcQE85ZEQZrA:1611846582544&source=lnms&tbm=isch&sa=X&ved=2ahUKEwit_O-39L7uAhXMyKQKHUOUC-0Q_AUoAXoECBIQAw&biw=1319&bih=693
    *Flowers:  https://www.google.com/search?q=red+roses+love&tbm=isch&ved=2ahUKEwj7j5O79b7uAhUYtKQKHZ1zBPEQ2-cCegQIABAA&oq=red+roses+love&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADIGCAAQCBAeOgcIIxDqAhAnOgQIIxAnOgQIABBDOgYIABAKEBhQihpYiUhg80toAnAAeACAAVCIAYQHkgECMTWYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=ydQSYLuHM5jokgWd55GIDw&bih=693&biw=1319
    *Keyholders: https://www.google.com/search?q=love+keyholder&sxsrf=ALeKk02VEBvBPZnuUgRRWWYieAW8rdzwnQ:1611846920942&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjWqJ7Z9b7uAhVM_aQKHQJ2AyoQ_AUoAXoECAUQAw&biw=1319&bih=693
    *https://www.google.com/search?q=chocolates+love&sxsrf=ALeKk01FsJtQAmt3AZYhIr7fTCZwri7p3Q:1611846995363&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjdvtz89b7uAhUJ66QKHXZNCOMQ_AUoAXoECBQQAw&biw=1319&bih=693
    *Pendants: https://www.google.com/search?q=pendants&sxsrf=ALeKk01j3V4-kUaweDA163nbnt2ljVQ47Q:1611847034950&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj35MyP9r7uAhXB6aQKHTY-DQIQ_AUoAXoECBcQAw&biw=1319&bih=693



<h3>Validators</h3>
The JSON Validator  https://jsonlint.com/






<h2>Tests</h2>

1. Test whether allauth is working properly, I run the server with a command: 'python3 manage.py runserver'
I opened the project and navidated to accounts/login. I tried to login using superuser and this directed me to the page asking for email confirmation. that this directs us back to a page telling us we need to confirm our email. So allauth is working because email confirmations are required in order to log in.

2. at the beginning of creating home and about pages in store app, I used HttpResponse to send some text to both pages to check if my setup is working.

3. I created a folder templates to contain all my html files, because django will look for temaplates by default

4. Creating home and about pages and testing them in a browser.

5. testing responsivness of desktop and mobile navbar in chrome dev tool by checking if all the features are nicely displayed on different screen sizes.

6. Tested json database with JSONLint https://jsonlint.com/ to check if it is properly written and matches category and product models.
7. Adding functionality to search bar and testing it by manuallu inserting key words from product description (search qurry working
8.Filtering by categories

8. I added a few products to my cart, then checked out
 using the test card number from stripe.
Everything went as expected and the form was submitted.
To make sure the payment went through I went to my stripe account's Events and saw that the payment was created.

<img src='/media/stripe_1.png' style="padding: 5px;">



9. since the checkout view doesn't have any handling for the post method.
Let's fix that in this video. So that when a user submits their payment information.
We also create the order in the database.
And redirect them to a success page.
The first thing to do is obviously check whether the method is post.
That means we should also wrap the current code into an else block to
handle the get requests.
In the post method code we will need the shopping bag.
And then we'll put the form data into a dictionary.
I'm doing this manually in order to skip the save infobox
which doesn't have a field on the order model.
All the other fields can come directly from the form though.
And then we can create an instance of the form using the form data.
If the form is valid we'll save the order.

Which it did.
And then let's check the admin to make sure the order was created properly.
Here in the admin, I see the order created with all the expected line items.

10. testingcard functionality using different card test number provided by stripe.

11. testing loading ovrlay

13.webhook_handlers



<h2>Installed packages</h2>
pip3 install Pillow

Creatied folders fixtures to load data into a django database very quickly, so we dont have to do it maniually in the admin,.