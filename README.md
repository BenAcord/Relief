Relief
=============
----------------------------------
 Paint the picture, tell the tale.
----------------------------------

About
=====
Relief structures an initial set of documentation from cyber security event or incident analysis.  It's primary purpose is to aid the handler in switching from left brain analysis to right brian social.  Specifically, to quicken the handler's answer to leadership's request, "give me a two slide summary of the event".

Relief is considered alpha software.  Complete enough for a minimum viable product but with the rough edges and lack of features that go with such a release.

The primary purpose for collecting summary facts and effects of the event is so that Relief can quickly generate consistently structured documentation for the handler.  Two documents are created from data collected: a presentation slide deck and a standard report document.  Currently, these are bare bones.

* **Presentation Slide Deck** - In an attempt to aid the handler, who may be deep in research, provide a brief slide deck for senior leadership or stakeholders on what is know about the event to-date.
  - All slides include:
    + Traffic light protocol markings as a warning for sharing
    + Customized footer for data handling and marking
  - The title slide acts as a warning to those who may not be authorized to view the content.
  - Executive Summary is the #1 slide for business-level communication on an event.  A convenient status bar exists to show which Cyber Kill Chain phases are known.
  - Each Cyber Kill Chain phase has two slides as supporting detail to the Executive Summary:
    + Business Impact and courses of action known for the phase
    + Diamond Model slide which includes the business impact and courses of action.  This is probably the #2 slide to show as you narrate the event.  Decide which phase is most crucial to protecting the stakeholders.

* **Document** - A skeleton to break the writers block when writing a final report or whitepaper on an event.
  - Follows a similar layout and structure as the slide deck but with boilerplate guides to expound and elaborate


Security Considerations
=======================
As previously mentioned Relief is a MVP, minimum viable product.  While the output is tagged for marking and handling the data and communication are not encrypted.  The SQLite database is cleartext.  Please use this information to secure your filesystem accordingly.


Installation & Setup
====================
Relief was coded and tested on Python 3.7.1.
See REQUIREMENTS.txt for the list of packages

1. Create a directory
2. Git clone the repo
3. Create and activate a Python3 virtual environment based on your OS
4. Install the dependencies: python3 -m pip install <list of items from REQUIREMENTS.txt>
5. Run Relief: python3 run.py
6. Open a browser and navigate to: http://localhost:5000

How to Use
==========
From the Home page of Relief you will have a description of the application functionality and several helpful references.  
There are three menu options across the top of the header.

* **New** - Create a new campaign name for an event being worked.
* **Campaigns** - A list of all previously created campaign events.  Each can be edited or deleted.  This is also where the documentation is generated.
* **Settings** - Defaults used in the creation of the documentation.  For example, change the file name prefix with your name or your company to have every file created with your brand.

Roadmap
=======
* Bug fixes: edit report date, possibly split this into a date range
* Remove obsolete code from pre-alpha tests
* Stats page with heatmap of strengths/weaknesses in collecting Cyber Kill Chain phases & Diamond Model data
* User supplied branded document templates instead of Python code to create output documents

end
