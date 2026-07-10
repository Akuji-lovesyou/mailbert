# mailbert
Email bot named mailbert that works in the cmdl interface. Can archive, mass delete and quickly delete emails with a preview quicker than the gmail website or app.

Mailbert is in a WIP stage at the moment

AS mailbert is updated I will edit the README with new info and setup information

To make a feature request make a issue with the header of FEATURE REQUEST and explain the feature you want. I will reply and let you know if i can add it. If addable I will close the ticket after the bot has been updated with your idea


As it stands the way to setup mailbert will need you to have a google cloud project with gmail api enabled and a OAuth token saved as a JSON added to the mailbert folder root with the name creds.JSON

After that has been setup run mailbert and allow him to access your gmail via the API after that rerun him and he should work.

Note that mailbert runs locally on your pc so there is no risk of leaking email informantion when using him.

Common issues
If you are getting errors when trying to auth mailbert the first time make sure that you have set your email as a test user of the application
Make sure you have set up the gmail api to allow all
If the bot fialed make sure to delete the created token file and rerun him after making said changes. 
If that doesnt work please make a issues ticket and I will look into it

