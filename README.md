<h1 align="center">CUPID STORE</h1>

[View the live project here.](https://codeinstitute.net)

This is the ecommerce website CUPID STORE designed to help customers buy gifts for their romantic dates. The website is fully responsive and was inspired by Boutique Ado Code Institute Tutorial. 

<h2 align="center"><img src='/media/ReadMe_image.jpg' style="margin: 0;"></h2>

<hr>
To navigate site as a logged in user, you may log in with the following:

Login: AnnaM <br>
Password: JuliaLittleGym

You can register for your own account using your real email, or if you prefer you may use a temporary one, which can be found at https://temp-mail.org/en/

* In order to view your order history you need to have a Cupid Store account.
<hr>

# 1. UX
### Project Goals
### Users Goals
### Site Owner's Goals
### Wireframes
### Design
### User Stories

# 2. Features

### Existing Features
### Features Left to Implement

# 3. Technologies Used

# 4. Testing
###  Manual Testing

# 5. Used Materials
# 6. Deployment

###  Github Deployment
### Heroku Deployment
# 7. Credits

# 8. Acknowledgements

<hr>

# 1. UX

### Project Goal 

The main goal of my website is to help a potential user to find quickly, without having to browes numerous pages, a  gift for his/her date.  

### Users Goals <br>
Each user visiting my site will be able to:

* Browse products within the store 
* Filter the products by categories and price
* See all products displayed on one page.
* Search products by key words
* Add products to the cart
* Remove products from the cart
* Go through checkout proccess
* To be able to place order with or without an account
* Sign up for an account
* Loginto his profile page to check or/and modify personal information
* See order history
* Leave a comment under a product (This feature still needs to be)fully developed

### Site Owner's Goals:

* Provide users with a safe and secure e-commerce platform in order to generate revenue from sales.
* Build awareness for the brand and attract new buyers.
* Collect user session data for market research purposes.
* Be able to add, edit or remove orders

### Wireframes 

 Here are the images of the wireframes, which I schetched out in my notebook before starting coding. Planning my project on the paper allowed me to visualize the final product and made it easier to execute it. 
<h2 align="center"><img src='/media/wireframes.JPG' style="margin: 0;"></h2>

### Design

 * Colour Scheme<br>
The four main colours used in my my site are light pink - for a site background, white - as some of image's background to make them stand out and dark grey - for text and the footer. Red often associated with love and passion is a predominant color of the Cupid Store products
<h2 align="center"><img src='/media/site_colors.png' style="margin: 0;"></h2>

 * Typography<br>
For the development pupposes I used rather neutral, commonly used fonts that are easy to read, but in the further site development I am planning to change some of the  fonts into more handwritting style, which create an ambiance of intimacy and give a more personal feeling to the site.

* Imagery<br>
The landing page is designed  to be striking and catch the user's attention with its warm and welcoming pink and stire curiosity and excitement with the red of two small hearts. A bit of glitter in the pink landing page background suggests luxury and promisses exciting shopping exxperience.

### User Stories<br>
* My friend Tom said "Cupid Store is a good idea for people who don't wnat to spend hours browsing through many different sites in search of a good first date gift. Everything is there, you just pick the one you like and it will be beautiffully wrapped and delivered to your place. So it does save you a lot of time and energy that you would have to otherwise spend on looking for it.
* Cupid Store was also appealing to younger users. My friends children would come and start browsing throug the website for toys. They found bears and chocolates almost irresistible. Some of them brought their piggy bank money and wanted to be the first customers of Cupud Store. 
* Kate, who likes to have evrything done her way commented:' I wouldn't mind sending a link of Cupid Store to my boyfriend and  maybe even suggesting him my gift preferences. That way I can get what I trully like and it also saves him a headache of wondering if I liked it or not.

# 2. Features
* Existing Features



Navbar<br>
The nav bar can be viewed on any of the pages of the webiste. From the nav bar, the user can navigate to the all_ products page, sort products by price and categories. By clicking on cart icon the user can go driectly to the cart page and see the products he has put in it. From Profile icone, the user can access login, logout, registaraton forms and Profile page depending on wether he is logein or not. Clicking on CUPID STORE logo will always take the user back to the all_products page.

Footer<br> Footer has the company owner name and a link to the github source code, but in the futre it will be replace with the company's contact details and a link to Customer service/or and Contact page.


All_Products page<br> 
On the products page which can be accessed via the "Shop Now" button from the landing page or via CUPID STORE LOGO link in the nav bar, the user can view all cupid gifts for sale on the website. The user can sort them by price and categories. By clicking on a selected image the user can access product detail page and get more information on the product he is interested in.

Detail Product page <br> 
The Detail product page contains all the information of the selected product such as: product's name, price, description and a product review section (still under construction)
From the product page, the user can add items directly to their cart and navigate to shopping cart page.
 

 Shopping cart page<br>
 Shopping cart page is the last step before the users navigates to the Checkoutpage to purchase his products. Here the user can check his cart content and make a final shopping decision. The user can remove the products he doesn't want in his cart by clicking on trash icon to, he can press the  continue shopping button or he he is satisfied with his shopping, he can press checkout button.

 Checkout page<br>
 On the checkout page, the user can see the summary of his purchase and a payment form, which needs to be filled in in order to buy the products.

Thank you page.<br>
 If the payment is successfuly processed, the user is redirected to the Thank You for shopping page where he can see detailed summary of his purchase.

If user decides to login, he can access his profile page with the order histry.

* Features to implement
Review<br> 
Finish working on Cuctomer Review section that is has been partially developped an is sitting at the bottom of Detai product page. I wrote a model and views for this feature, but it was was not working properly, so I removed Review related code and left only the form for the future development. 

Contact Page<br>
Currently there is no contact sesction, but I would like to create  a a page where customers can go and make enquiry about a product or service. The page should also include company's address and a Customer Service telephone number,  

Gift Wrapping section<br>
Gifts are given for a special ocassions for people we love and care about and every gift should be neatly packaged or come in a nice box. Part of my development plan for the site is to add wrapping service where custommers could pick gift wrapping of their preference.

# 3. Technologies Used

### Languages: 
        HTML5 <br> 
        CSS<br> 
        JavaScript<br>
        Python v 3.8.6<br>
### Libraries:        
        jQuery v 3.5.3<br>
### Frameworks:<br> 
        django v 1.11.29<br>
### Others<br>
Bootstrap was used to build and style the website.<br>
Google Fonts<br>
HerokuAWS3<br>
Stripe -to implement payment features
Photo image resizer

# 4. Testing

### Test made during app development

1. Test whether allauth is working properly, I run the server with a command: 'python3 manage.py runserver'
I opened the project and navidated to accounts/login. I tried to login using superuser and this directed me to the page asking for email confirmation. that this directs us back to a page telling us we need to confirm our email. So allauth is working because email confirmations are required in order to log in.

2. At the beginning of creating home and about pages in my store app, I used HttpResponse to send some text to both pages to check if my setup is working.

3. I created a folder templates to contain all my html files, because django will look for temaplates by default

4. Creating home and about pages and testing them in a browser.

5. Testing responsivness of desktop and mobile navbar in chrome dev tool by checking if all the features are nicely displayed on different screen sizes.

6. Tested json database with JSONLint https://jsonlint.com/ to check if it is properly written and matches category and product models.

7. Adding functionality to search bar and testing it by manuallu inserting key words from product description to see if search qurry is working.  

8. Checking payment functionality. I added a few products to my cart, then checked out and paid using the test card number from stripe. Everything went as expected and the form was submitted. To make sure the payment went through I went to my stripe account's Events and saw that the payment was created.

<img src='/media/stripe_1.png' style="padding: 5px;">

9. testing loading ovrlay. It didn't load well first time, but after hard reloading it started working.

10. Veryfing that webhooks came from stripe. First, I set up the stripe API key and next the webhook secret, which I needed to verify that the webhook actually came from stripe. To confirm the webhook view is working I printed out "success" in my terminal and then return a 200 response.

<img src='/media/webhooks.png' style="margin: 0;">

This means that anytime stripe sends me a webhook it lets me know that an event has occurred.
I have effectively set up a listener to listen to messages from stripe.

11. To verifying that my webhook work properly. Due to a faulty wh link my first attempts failed, but the senond one was a success.

<img src='/media/webhooks_attemps.png' style="margin: 0;">

12. Payment intent testing. Ok.

13. Testing payment system with differnt test card numbers provided by Stripe.
 To test the stripe payment system, I filled out billing address form and used 4242424242424242 (CVC any 5 digits) test card numbers, tyoed in a valid expiration date in the future, and a random CVC number. It all went well and a successful payment was created.

I repeated the same test with 2 other acrds:

    5555555555554444	Mastercard  CVC (Any 5 digits).  test: passed
    378282246310005	American Express CVC (Any 5 digits).  test: passed

 14. Testing checkout form with wrong details. I tested checkout form by purposely entering wrong information (wrong CVS-too short or too long, ..etc) or didn't provide required information like name or country. As expected each time I would get an error message.

15. Testing manually fuctionality of all the Cupid Store's features by loging into the page, selecting a product, navigating to checkout and paying for it with a test card number. Checking the profile page for the history record.

### TESTING TOOLS
The following testing tools were used to minimize site errors:

W3C Markup Validator
W3C CSS Validator
pyTest
PEP8
Diffchecker
HTML Formatter
Language Tool
CSS Beautyfier

### Notes

HTML
I passed my HTML code through the W3C Markup Validation Service. I had some unclosed tags,andother minor erors that thanks to the valodator I could easly spoit and correct.

CSS
I checked all CSS code with the W3C Markup Validation Service. All individual CSS files passed without any errors.

JavaScript
I used JSHint to check my JavaScript code. 

Python
For this project I installed PEP8 on my gitpod, which made it faster to spot any errors. As expected I always had a few indentation errors and warnings that some lines were too long.  

### Compatibility tests
Using different browsers
I manually tested the project on the following web browsers, checking that all aspects worked as planned:

Google Chrome
Apple Safari

### Using different devices

The project has been tested on the following devices:
<h2 align="center"><img src='/media/testing_responsivness.png' style="margin: 0;"></h2>

I found it quite challenging to make my app equally responsive on all devices. It would probably require a way more time to test every single aspect of the app on many different devices.

















# 5. Used Materials

* Bootstrap 4 Cheat Sheet
https://hackerthemes.com/bootstrap-cheatsheet/
https://bootstrapcreative.com/resources/bootstrap-4-css-classes-index/

* Footer-taken from bootstrap4 and modified
https://mdbootstrap.com/docs/standard/navigation/footer/

* All the images were found on Google. I think I habve gone throught 50 to 60 various toy, chocolate, keyholders, flowers and pendants making companies.
    *Bears:  https://www.google.com/search?q=bears+love&sxsrf=ALeKk00FoCv0GiP7ycyTnlGcQE85ZEQZrA:1611846582544&source=lnms&tbm=isch&sa=X&ved=2ahUKEwit_O-39L7uAhXMyKQKHUOUC-0Q_AUoAXoECBIQAw&biw=1319&bih=693
    *Flowers:  https://www.google.com/search?q=red+roses+love&tbm=isch&ved=2ahUKEwj7j5O79b7uAhUYtKQKHZ1zBPEQ2-cCegQIABAA&oq=red+roses+love&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADIGCAAQCBAeOgcIIxDqAhAnOgQIIxAnOgQIABBDOgYIABAKEBhQihpYiUhg80toAnAAeACAAVCIAYQHkgECMTWYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=ydQSYLuHM5jokgWd55GIDw&bih=693&biw=1319
    *Keyholders: https://www.google.com/search?q=love+keyholder&sxsrf=ALeKk02VEBvBPZnuUgRRWWYieAW8rdzwnQ:1611846920942&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjWqJ7Z9b7uAhVM_aQKHQJ2AyoQ_AUoAXoECAUQAw&biw=1319&bih=693
    *https://www.google.com/search?q=chocolates+love&sxsrf=ALeKk01FsJtQAmt3AZYhIr7fTCZwri7p3Q:1611846995363&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjdvtz89b7uAhUJ66QKHXZNCOMQ_AUoAXoECBQQAw&biw=1319&bih=693
    *Pendants: https://www.google.com/search?q=pendants&sxsrf=ALeKk01j3V4-kUaweDA163nbnt2ljVQ47Q:1611847034950&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj35MyP9r7uAhXB6aQKHTY-DQIQ_AUoAXoECBcQAw&biw=1319&bih=693

Other Inspiration and Sources

* Code Institute Ecommerce Boutique project, which I used as themain inspiration for my project. Boutique Ado is a beautifully developped app and I used it as a template for my project. 
* StackOverflow for refference on solving similar bugs and in search for interesting code solutions
* Youtube videos 
* Django Official Website
* Udemy courses


Django Official Website
Youtube videos and Udemy courses

# 8. Acknowledgements

A big thank you to Code Institute for providing well structured  educational  material. Thank you to all the tutors for their immense patience and assistance in solving the bugs. And special thank you to my Australian mentor Anna Villanueva for her support and feedback on my project adventure.





 [View](https://github.com/)

    -   Contact Us Page Wireframe - [View](https://github.com/)

## Features

-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
    - Photoshop was used to create the logo, resizing images and editing photos for the website.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the organisation.

        1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath there is a Hero Image with Text and a "Learn More" Call to action button.
        2. The main points are made immediately with the hero image
        3. The user has two options, click the call to action buttons or scroll down, both of which will lead to the same place, to learn more about the organisation.

    2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.

        1. The site has been designed to be fluid and never to entrap the user. At the top of each page there is a clean navigation bar, each link describes what the page they will end up at clearly.
        2. At the bottom of the first 3 pages there is a redirection call to action to ensure the user always has somewhere to go and doesn't feel trapped as they get to the bottom of the page.
        3. On the Contact Us Page, after a form response is submitted, the page refreshes and the user is brought to the top of the page where the navigation bar is.

    3. As a First Time Visitor, I want to look for testimonials to understand what their users think of them and see if they are trusted. I also want to locate their social media links to see their following on social media to determine how trusted and known they are.
        1. Once the new visitor has read the About Us and What We Do text, they will notice the Why We are Loved So Much section.
        2. The user can also scroll to the bottom of any page on the site to locate social media links in the footer.
        3. At the bottom of the Contact Us page, the user is told underneath the form, that alternatively they can contact the organisation on social media which highlights the links to them.

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to find the new programming challenges or hackathons.

        1. These are clearly shown in the banner message.
        2. They will be directed to a page with another hero image and call to action.

    2. As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.

        1. The navigation bar clearly highlights the "Contact Us" Page.
        2. Here they can fill out the form on the page or are told that alternatively they can message the organisation on social media.
        3. The footer contains links to the organisations Facebook, Twitter and Instagram page as well as the organization's email.
        4. Whichever link they click, it will be open up in a new tab to ensure the user can easily get back to the website.
        5. The email button is set up to automatically open up your email app and autofill there email address in the "To" section.

    3. As a Returning Visitor, I want to find the Facebook Group link so that I can join and interact with others in the community.
        1. The Facebook Page can be found at the footer of every page and will open a new tab for the user and more information can be found on the Facebook page.
        2. Alternatively, the user can scroll to the bottom of the Home page to find the Facebook Group redirect card and can easily join by clicking the "Join Now!" button which like any external link, will open in a new tab to ensure they can get back to the website easily.
        3. If the user is on the "Our Favourites" page they will also be greeted with a call to action button to invite the user to the Facebook group. The user is incentivized as they are told there is a weekly favourite product posted in the group.

-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if there are any newly added challenges or hackathons.

        1. The user would already be comfortable with the website layout and can easily click the banner message.

    2. As a Frequent User, I want to check to see if there are any new blog posts.

        1. The user would already be comfortable with the website layout and can easily click the blog link

    3. As a Frequent User, I want to sign up to the Newsletter so that I am emailed any major updates and/or changes to the website or organisation.
        1. At the bottom of every page their is a footer which content is consistent throughout all pages.
        2. To the right hand side of the footer the user can see "Subscribe to our Newsletter" and are prompted to Enter their email address.
        3. There is a "Submit" button to the right hand side of the input field which is located close to the field and can easily be distinguished.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   On some mobile devices the Hero Image pushes the size of screen out more than any of the other content on the page.
    -   A white gap can be seen to the right of the footer and navigation bar as a result.
-   On Microsoft Edge and Internet Explorer Browsers, all links in Navbar are pushed upwards when hovering over them.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   The full-screen hero image code came from this [StackOverflow post](https://stackoverflow.com)

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

-   [MDN Web Docs](https://developer.mozilla.org/) : For Pattern Validation code. Code was modified to better fit my needs and to match an Irish phone number layout to ensure correct validation. Tutorial Found [Here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel#Pattern_validation)

### Content

-   All content was written by the developer.

-   Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

### Media

-   All Images were created by the developer.

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.