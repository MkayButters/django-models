## TO DO: 


- add model to admin
    - modify Post model have user friendly display in admin
    - create migrations and migrate data
    - create a super user
- Add a few posts via Admin panel

- Addtemplates folder in root of project
    - register templates folder in project settings
    - create HomePageView
    - extend ListView
give a template of home.html
associate Post model
create home.html template
use Django Templating Language to display each post’s title
create base.html ancestor template
add main html document
use Django Templating Language to allow child templates to insert content
update url patterns for app and project
view home page and confirm posts showing properly
add detail view
link post_detail.html template
associate Post model
create post_detail.html template
template should extend base
content should display post title and body
update app urlpatterns to handle detail view
account for primary key in url
add link in home page template to related post detail page

- Test HomePageViewTest
    - verify status code
    - verify correct template use
    - use url name instead of hard coded path
