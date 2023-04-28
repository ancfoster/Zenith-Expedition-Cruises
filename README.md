# Zenith-Expedition-Cruises

This project involved developing an e-commerce website for the imaginary cruise line, Zenith Expedition Cruises. The website is built using the Django MVT framework and allows users to find and book an expedition cruise.
The project involved devloping a comprehensive booking management system for the cruise company, kown as Cruise Manager. This booking management system keeps track of inventory (tickets) and manages which suites are booked on any given cruise. It also features an enquiry management system. 

- **[Deployed Site](https://zenith-ci.herokuapp.com/)**

![screenshot](readme_assets/responsive.jpeg)


## Design Process

In this section, you will briefly explain your design processes.

### Colour Scheme

- Both the custom admin interfaces and the customer front end site both use a monochrome colour scheme, consisting of different shades of grey and black.

- The colour choices are for aesthetic purposes but to also convey importance of different UI elements through visual hierachy. Headings or labels with a lighter colour are less important than those with a darker shade. 

![screenshot](readme_assets/colours.jpeg)

In my main `main.css` I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

![screenshot](readme_assets/root.jpeg)

### Typography

For this project I used fonts from Adobe Fonts and added them using `@import` inside my CSS.

- [Termina](https://fonts.adobe.com/fonts/termina) was used for the primary headers and titles.

	![screenshot](readme_assets/termina.jpeg)

- [Neue Haas Grotesk](https://fonts.adobe.com/fonts/neue-haas-grotesk) was used for body text and labels

	![screenshot](readme_assets/neue.jpeg)

- [Forma DJR](https://fonts.adobe.com/fonts/forma-djr-micro) was used for he typography for the Cruise Manager Admin Interface

	![screenshot](readme_assets/forma.jpeg)


### Icons

- For this project I used [Google's Material Design Icon library](https://fonts.google.com/icons) for icons. These were implented by importing a Google Stylesheet and applying it to spans where I would write out the name of the icon.

- Here is an example of how icons are used to respresent information to the user in an intuitive way that allows for less text labels.

	![screenshot](readme_assets/icons.jpeg)

- I also made my own custom favicon featuring the company's logo mark.

	![screenshot](readme_assets/favicon.png)


## Agile

Agile is a project management methodology that emphasizes flexibility, collaboration, and rapid iteration. It is designed to help teams quickly adapt to changing requirements and deliver value to customers in a more efficient and effective manner. Agile involves breaking down large projects into smaller, more manageable tasks, and continuously testing and refining the product throughout the development process.

To help me manage the planning and implementation of all primary functionality with the agile methodology I used the [monday.com agile prroject management tool](https://monday.com/features/kanban).

### Agile User Story Boards

- In Agile software development, user stories are used to capture the requirements for a particular feature or piece of work. They are typically written from the perspective of an end user using the format:
    - As a **role** I can **functionality** so that **benefit**

- I also made use of MoSCoW prioritization, a technique commonly used in Agile project management to prioritize project requirements based on their importance. The acronym stands for "Must have," "Should have," "Could have," and "Won't have." The technique helps project teams to focus on the most critical and essential requirements first, ensuring that the project delivers the highest value to the stakeholders.

	- The "Must have" requirements are those that are essential for the project's success, and failure to deliver them would result in a significant impact on the project's overall value.

	- The "Should have" requirements are important but not critical, and they can be postponed if necessary.
		
	- The "Could have" requirements are desirable but not necessary, and they can be deferred to a later phase or iteration. The "Won't have" requirements are those that the project team has agreed not to include in the current scope.


#### Customer user story board

![screenshot](readme_assets/user_board.jpeg)


#### Site owner story board

![screenshot](readme_assets/business_board.jpeg)

### Kanban Board

- A Kanban board in Agile is a visual project management tool that provides an overview of the workflow, allowing team members to visualize and manage their work more efficiently.

- I used the Kanban board to 'move' stories between the columns of to do, in progress and done.

![screenshot](readme_assets/kanban.png)

### User Stories & Features

#### Customer user stories

- As a user I can create an account so that I can book a cruise
- As a user I can login into my account so that I can make a booking
- As a user I can browse through a list of cruises so that I can see there any cruises that interest me.
- As a user I can view detailed information about a cruise so that I can learn more about that cruise and see if it is a cruise I want to book.
- As a user I can book a cruise on the website so that I can book a cruise any time of day without having to contact the company via phone.
- As a user I can filter available cruises so that I can only the most relevant ones.
- As a user I can use a credit card to pay for my cruise securely.
- As a user I can see which suites are available for me to book.
- As a user I can unsubscribe to marketing emails when I am no longer interested in them
- As a user I can subscribe to marketing emails so that I can receive Zenith company news and promotional offers.
- As a user I can send an enquiry message so that I can contact the company if I have any questions
- As a user I can use a navigation bar so that I can easily navigate through the site.

#### Site owner stories

- As a site owner I can reduce site storage, bandwidth and improve SEO by having images compressed on upload
- As a site owner I can improve the site's SEO through a sitemap so that i can improve the company's search ranking
- As a site owner I can edit cruise prices through a custom interface so that I can boost sales.
- As a site owner I can add new cruise destinations so that I can create new itineraries
- As a site owner I can view revenue generated through online bookings so that I can monitor sales.
- As a site owner I can see customer enquiries in a list so that I can easily keep track of them and respond to them
- As a site owner I can use a Facebook Page so that I can market the company on a popular social media platform.
- As a site owner I will use an admin dashboard so that I can to see key business information like revenue, number of bookings and quickly access key tasks
- As a site owner I can view the details of an existing booking so that I can see which customers are booked on a specific cruise.
- As a site owner I can access a custom manager interface so that employees can interact through an easy to use interface and not the Django admin

## Site Features

### Cruise Manager Admin Features

- My project includes a stock management system in the background. When a cruise is created, tickets are automatically generated based on the suites and suite categories tables. When a customer makes a booking a ticket is marked as booked so that a customer cannot double book it. If a booking is deleted in the cruise manager interface the ticket comes available to book again.

| Feature | Description | Screenshot |
| --- | --- | --- |
| Button to access cruise manager when user is a 'staff user' | A conditional button only appears when the user is signed in as a staff user. This provides access to the Cruise manager dashboard | ![screenshot](readme_assets/button.jpeg) |
| Dashboard | Provides key business statistics and links to common actions | ![screenshot](readme_assets/dashboard.jpeg) |
| Cruise List | Provides a list of cruises in the database. Clicking on a cruise brings up detail view | ![screenshot](readme_assets/cruises_admin.jpeg) |
| Cruise Detail View | Provides a detail view of a specific cruise and links to Edit/Delete | ![screenshot](readme_assets/admin_cruise_detail.jpeg) |
| Cruise Delete View | Provides a view to delete a cruise | ![screenshot](readme_assets/cruise_delete.jpeg) |
| Cruise Edit View | Provides view to edit cruise prices and details | ![screenshot](readme_assets/cruise_edit.jpeg) |
| Cruise Create View | Provides view to create a new cruise, which generates tickets| ![screenshot](readme_assets/cruise_create.jpeg) |
| Destinstion list | Lists destinations in the database and links to detail view and ot create one | ![screenshot](readme_assets/destination_list.jpeg) |
| Destinstion detail view | Shows details of a destination and provides links to edit/delete views. | ![screenshot](readme_assets/desti_detail.jpeg) |
| Destinstion edit view | Provides a way to edit a destination in the database | ![screenshot](readme_assets/edit_desti.jpeg) |
| Destinstion delete view | Provides a way to delete a destination from the database | ![screenshot](readme_assets/delete_desti.jpeg) |
| Tag view | Tags are a way for users to filter cruises. This view shows a list of tags in the system with buttons to create, edit, delete | ![screenshot](readme_assets/tag_view.jpeg) |
| Tag delete view | Provides a way to delete a tag from the database | ![screenshot](readme_assets/delete_tag.jpeg) |
| Booking list | Lists bookings in the system, providing a link to see booking details | ![screenshot](readme_assets/booking_list.jpeg) |
| Booking detail view | Shows details of a specific booking and the amount paid. Shows a delete action button. | ![screenshot](readme_assets/booking_detail.jpeg) |
| Booking delete view | Provides a way to delete a booking and make the associated ticket available for booking again | ![screenshot](readme_assets/delete_booking.jpeg) |
| Enquiry list | Shows a list of customer enquiries from the contact form. Shows how many need responding to by staff with a status icon | ![screenshot](readme_assets/enquiry_list.jpeg) |
| Enquiry message view | Shows the enquiry message and provides action buttons for marking as responded to and deletion. | ![screenshot](readme_assets/enquiry_message.jpeg) |


### Customer Features

| Feature | Description | Screenshot |
| --- | --- | --- |
| Sign in | Login for those with an account | ![screenshot](readme_assets/login.jpeg) |
| Sign up | Create an account | ![screenshot](readme_assets/signup.jpeg) |
| Navigation bar | To navigate around site and access login/logout | ![screenshot](readme_assets/nav.jpeg) |
| Home page| Conveys to new visitors what the company does and links to other pages | ![screenshot](readme_assets/home.jpeg) |
| Experience page| Informs users of the onboard experience | ![screenshot](readme_assets/exp.jpeg) |
| Contact form| Allows unregistered and registered users to contact the company 24/7 with a form | ![screenshot](readme_assets/contact_form.jpeg) |
| Subscribe to marketing email | Allows users to receieve news and offers by email | ![screenshot](readme_assets/subscribe.jpeg) |
| See available cruises in a list | Allows users to see bookable cruises, with key information like dates, starting price and ship | ![screenshot](readme_assets/cruise_results.jpeg) |
| Filter cruise list by tag | See available cruises based on interest, display what filter has been applied | ![screenshot](readme_assets/filter.jpeg) |
| Detailed cruise view | View more detailed information about a cruise including the destinations and all pricing options | ![screenshot](readme_assets/cruise_view.jpeg) |
| Booking process | A step by step booking flow guides the user through making a booking, including selecting a suite category and suite with dynamic pricing | ![screenshot](readme_assets/booking.jpeg) |
| Available suites | Whilst booking a cruise the site shows which suites are available to book | ![screenshot](readme_assets/suites.jpeg) |
| Payment| User can pay with using Stripe form | ![screenshot](readme_assets/payment.jpeg) |
| Confirmation | Upon a successful booking the user is presented with a confirmation and booking number | ![screenshot](readme_assets/disp_conf.jpeg) |
| Confirmation email | The user receives a confirmation email after they have made a booking | ![screenshot](readme_assets/email_conf.jpeg) |


## Wireframes


## Technologies & Tools Used

### Front-End

- HTML5 - hypertext markup language is the standard language for designing files to be displayed in a web browser like Chrome or Safari. 

- CSS3 - cascading style sheets is a language used for styling a file written in a markup language like HTML.

- JavaScript (ES11) is a scripting language and one of the main technologies of web development. In this project it was used on the client side for webpage behavior.

- Tailwind - Tailwind is used for creating utility CSS styles for styling cruise manager. Tailwind is a utility-first CSS framework that provides a set of pre-designed CSS classes to speed up the development process.

### Back-End

- [Django](https://www.djangoproject.com/) an open-source, Python-based web framework that follows the model–template–views (MTV) architectural pattern.

- [PostgreSQL](https://www.postgresql.org/) is an open-source relational database management system (RDBMS)

- [Python](https://www.python.org/) is a high-level, general-purpose programming language and was used for the backend. The use of Django as the selected framework dictated the use of Python.

- [Heroku](https://heroku.com/) is a cloud platform as a service (PaaS) supporting several programming languages and database. Heroku is used to host the deployed application and PostgreSQL database.

- [AWS S3](http://aws.amazon.com/s3/) was used for hosting the Django static files and user uploaded media. Amazon Simple Storage Service is a service offered by Amazon Web Services (AWS) that provides object storage through a web service interface.

### Packages Used

Further details on all Python packages used on this project can be found in the requirements.txt file.
| Package | Version | Description |
|---|---|---|
| asgiref | 3.5.2 | ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI. |
| backports.zoneinfo | 0.2.1 | Backport of the standard library module zoneinfo |
| boto3 | 1.26.12 | Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2 |
| botocore | 1.29.12 | A low-level interface to a growing number of Amazon Web Services. The botocore package is the foundation for the AWS CLI  |
| dj-database-url | 1.0.0 | Allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application. |
| Django | 3.2.16 | Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. |
| django-allauth | 0.51.0 | Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication. |
| django-multiupload | 0.6.1 | Simple drop-in multi file upload field for django forms using HTML5's multiple attribute. |
| django-storages | 1.13.1 | Adds support for storage backends in Django |
| gunicorn | 20.1.0 | A Python WSGI HTTP Server for UNIX. |
| jmespath | 1.0.1 | JSON Matching Expressions |
| oauthlib | 3.2.2 | A generic, spec-compliant, thorough implementation of the OAuth request-signing logic |
| Pillow | 9.3.0 | Python Imaging Library adds image processing capabilities |
| psycopg2-binary | 2.9.5 | PostgreSQL database adapter for the Python programming language |
| PyJWT | 2.6.0 | JSON Web Token implementation in Python |
| python3-open-id | 3.2.0 | A set of Python packages to support use of the OpenID decentralized identity system |
| pytz | 2022.7 | Accurate and cross platform timezone calculations |
| requests-oauthlib | 1.3.1 | Provides OAuth library support for requests |
| s3transfer | 0.6.0 | For managing Amazon S3 transfers |
| sqlparse | 0.4.3 | A non-validating SQL parser. |
| stripe | 5.4.0 | Integrates Stripe into Python/Django project |


## Database Schema

### Diagram

![Database diagram](readme_assets/schema.jpeg)

### Database Models

Zenith Expedition Cruises is made of 4 custom applications and 11 models, in addition to the user model that comes with the Django admin/authentication system

### Models and fields

- Destination
	name: CharField
	country: CountryField
	continent: CharField
	description: TextField
	image: ImageField
	latitude: DecimalField
	longitude: DecimalField

- Ships
	name: CharField
	total_suites: PositiveSmallIntegerField
	info_page: URLField
	ship_image: ImageField

- SuiteCategories
	name: CharField
	description: TextField
	sleeps: PositiveSmallIntegerField
	size: PositiveSmallIntegerField
	suite_image: ImageField
	suite_layout_image: ImageField
	suite_feature_list: CharField
	category_deckplan: ImageField


- Suites
	ship: ForeignKey to Ships
	suite_num_name: CharField
	category: ForeignKey to SuiteCategories

- Tag
	name: CharField

- Cruises
	name: CharField
	ship: ForeignKey to Ships
	created_on: DateTimeField
	duration: PositiveSmallIntegerField
	start_date: DateField
	end_date: DateField
	description: TextField
	results_image: ImageField
	listing_image: ImageField
	map_image: ImageField
	bookable: BooleanField
	tags: ManyToManyField to Tag
	port_number: PositiveSmallIntegerField
	slug: SlugField

- Fares model
	cruise: ForeignKey relationship to Cruises model
	suite_category: ForeignKey relationship to SuiteCategories model
	price: Decimal field

- Movements model
date: Date field
type: Char field with choices
ship: ForeignKey relationship to Ships model
destination: ForeignKey relationship to Destination model
cruise: ForeignKey relationship to Cruises model
order: PositiveSmallIntegerField with validators
description: Char field 

- Tickets model
	ticket_ref: Char field
	ship: ForeignKey relationship to Ships model
	cruise: ForeignKey relationship to Cruises model
	booked: Boolean field
	suite: ForeignKey relationship to Suites model
	created_on: DateTime field 

- Bookings model
	booking_ref: Char field
	booked_by: ForeignKey relationship to User model 
	number_of_guests: PositiveSmallIntegerField
	booking_price: Decimal field
	booked_on: DateTime field 
	ticket: ForeignKey relationship to Tickets model
	cruise_name_str: Char field 
	guests: Char field


## Ecommerce Business Model

This site sells goods to individual customers, and therefore follows a `Business to Customer` model. By having an ecommerce website Zenith Expedition Cruises is able to take new bookings 24 hours a day. 

It is still in its early development stages, although it already has a newsletter, and links for social media in the footer marketing.

Social media can potentially build a community of users around the business, and boost site visitor numbers,
especially when using larger platforms such a Facebook.

A newsletter list can be used by the business to send regular messages to site users.
For example, what items are on special offer, new items in stock,
updates to business hours, notifications of events, and much more!

## Search Engine Optimization (SEO) & Social Media Marketing

### Keywords & Description Meta Fields

I've identified some appropriate keywords to align with my site, that should help users
when searching online to find my page easily from a search engine.
I have added the keyword and meta fields to the head section to improve SEO.

![meta fields in head](readme_assets/meta.jpeg)

### Sitemap

- I've used Djano's built in sitemap application to generate a sitemap automatically.

- The sitemap can be be viewed at [https://zenith-ci.herokuapp.com/sitemap.xml](https://zenith-ci.herokuapp.com/sitemap.xml)

### Robots

I've created the [robots.txt](robots.txt) file at the root-level.

It can be seen at [https://zenith-ci.herokuapp.com/robots.txt](https://zenith-ci.herokuapp.com/robots.txt)

- `User-agent: *
Disallow:
Sitemap: https://zenith-ci.herokuapp.com/sitemap.xml`


### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales.
Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

= I've created a Facebook page to promote the company:

![screenshot](readme_assets/facebook.jpeg)

- In the footer there are links to popular social media sites

![screenshot](readme_assets/socials.jpeg)

### Newsletter Marketing

I have incorporated a newsletter sign-up form on my application so that they can keep upto date with the latest news and promotional offers. I have implemented this via MailChimp as:

- MailChimp handle the GDPR requirements and make it easy for users to unsubscribe
- MailChimp includes an email campaign builder, this makes it easy for non-technical staff at Zenith Expedition Cruises to produce emails.

![screenshot](readme_assets/mailchimp.jpeg)

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://zenith-ci.herokuapp.com/).

### ElephantSQL Database

This project uses Heroku for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: Zenith-Expedition-Cruises).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Amazon AWS

This project uses [AWS](https://aws.amazon.com) to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
	- Suggested Name: `group-zenith-expedition-cruises` (group + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::your-bucket-name",
						"arn:aws:s3:::your-bucket-name/*"
					]
				}
			]
		}
		```
	
	- Click **Review Policy**.
	- Suggested Name: `policy-zenith-expedition-cruises` (policy + the project name)
	- Provide a description:
		- "Access to S3 Bucket for zenith-expedition-cruises static files."
	- Click **Create Policy**.
- From **User Groups**, click your "group-zenith-expedition-cruises".
- Click **Attach Policy**.
- Search for the policy you've just created ("policy-zenith-expedition-cruises") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Suggested Name: `user-zenith-expedition-cruises` (user + the project name)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `group-zenith-expedition-cruises`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
	- **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://fff.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or Zenith-Expedition-Cruises
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = your new 16-character API key
	- `EMAIL_HOST_USER` = your own personal Gmail email address (`you@gmail.com`)

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | insert your own AWS Access Key ID key here |
| `AWS_SECRET_ACCESS_KEY` | insert your own AWS Secret Access key here |
| `DATABASE_URL` | insert your own ElephantSQL database URL here |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | insert your own Gmail API key here |
| `EMAIL_HOST_USER` | insert your own Gmail email address here |
| `SECRET_KEY` | this can be any random secret key |
| `STRIPE_PUBLIC_KEY` | insert your own Stripe Public API key here |
| `STRIPE_SECRET_KEY` | insert your own Stripe Secret API key here |
| `STRIPE_WH_SECRET` | insert your own Stripe Webhook API key here |
| `USE_AWS` | True |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "insert your own AWS Access Key ID key here")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "insert your own AWS Secret Access key here")
os.environ.setdefault("DATABASE_URL", "insert your own ElephantSQL database URL here")
os.environ.setdefault("EMAIL_HOST_PASS", "insert your own Gmail API key here")
os.environ.setdefault("EMAIL_HOST_USER", "insert your own Gmail email address here")
os.environ.setdefault("SECRET_KEY", "this can be any random secret key")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "insert your own Stripe Public API key here")
os.environ.setdefault("STRIPE_SECRET_KEY", "insert your own Stripe Secret API key here")
os.environ.setdefault("STRIPE_WH_SECRET", "insert your own Stripe Webhook API key here")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:
- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/ancfoster/Zenith-Expedition-Cruises) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/ancfoster/Zenith-Expedition-Cruises.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ancfoster/Zenith-Expedition-Cruises)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ancfoster/Zenith-Expedition-Cruises)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

Use this space to discuss any differences between the local version you've developed, and the live deployment site on Heroku.

## Credits


### Tutorials followed


| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder) | README and TESTING | Tool to help generate the Markdown files |
| [Jaysha](https://ordinarycoders.com/blog/article/django-sitemap) | Django sitemap | How to Create a Dynamic Django Sitemap |
| [Code with Stein](https://codewithstein.com/adding-robots-txt-to-a-django-site/) | Adding robots.txt | Adding robots.txt to a Django site |


### Media

Use this space to provide attribution links to any images, videos, or audio files borrowed from online.
A few examples have been provided below to give you some ideas.

If you're the owner (or a close acquaintance) of all media files, then make sure to specify this.
Let the assessors know that you have explicit rights to use the media files within your project.

Ideally, you should provide an actual link to every media file used, not just a generic link to the main site!
The list below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links
by sending yourself the following command: `!freemedia`.

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com) | entire site | image | favicon on all pages |
| [Lorem Picsum](https://picsum.photos) | home page | image | hero image background |
| [Unsplash](https://unsplash.com) | product page | image | sample of fake products |
| [Pixabay](https://pixabay.com) | gallery page | image | group of photos for gallery |
| [Wallhere](https://wallhere.com) | footer | image | background wallpaper image in the footer |
| [This Person Does Not Exist](https://thispersondoesnotexist.com) | testimonials | image | headshots of fake testimonial images |
| [Audio Micro](https://www.audiomicro.com/free-sound-effects) | game page | audio | free audio files to generate the game sounds |
| [Videvo](https://www.videvo.net/) | home page | video | background video on the hero section |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |

### Acknowledgements

Use this space to provide attribution to any supports that helped, encouraged, or supported you throughout the development stages of this project.
A few examples have been provided below to give you some ideas.

- I would like to thank my Code Institute mentor, Tim Nelson for their support throughout the development of this project and the whole of my CI diploma. Their guidance has been invaluable.
- I would like to thank my wife Alice for extensively testing the site and providing feedback.
