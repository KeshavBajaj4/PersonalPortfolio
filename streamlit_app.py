import streamlit as st
import requests

# Custom CSS styling
st.markdown(
    """
    <style>
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        background-color: #f5f5f5;
        color: #333;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        position: sticky;
        top: 0;
        z-index: 999;
    }
    .navbar-brand {
        font-size: 1.5rem;
        font-weight: bold;
        color: #333;
        text-decoration: none;
    }
    .nav-links {
        display: flex;
        gap: 2rem;
        list-style-type: none;
        margin: 0;
        padding: 0;
    }
    .nav-link {
        color: #333;
        text-decoration: none;
        font-weight: bold;
        font-size: 1.2rem;
        padding: 0.5rem 1rem;
    }
    .nav-link:hover {
        background-color: #333;
        color: #fff;
        border-radius: 5px;
    }
    .section {
        padding: 2rem;
        background-color: #f5f5f5;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        animation: float 5s infinite;
    }
    @keyframes float {
        0% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-10px);
        }
        100% {
            transform: translateY(0);
        }
    }
    .title {
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-align: center;
    }
    .content {
        font-size: 1.2rem;
        line-height: 1.6;
    }
    .portfolio-item {
        margin-bottom: 1rem;
        padding: 1rem;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .portfolio-item-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .portfolio-item-description {
        margin-bottom: 1rem;
    }
    .portfolio-item-link {
        display: inline-block;
        font-weight: bold;
        color: #333;
        text-decoration: none;
        background-color: #f5f5f5;
        padding: 0.5rem 1rem;
        border-radius: 5px;
    }
    .portfolio-item-link:hover {
        background-color: #333;
        color: #fff;
    }
    .form-container {
        padding: 1rem;
        background-color: #f5f5f5;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .form-label {
        font-weight: bold;
    }
    .form-input {
        margin-bottom: 1rem;
    }
    .form-save-button {
        display: flex;
        justify-content: flex-end;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page: Home
def home_page():
    st.title("Welcome to My Portfolio")
    st.write("Here, you can explore my work and qualifications.")


# Page: Portfolio
def portfolio_page():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='title'>Portfolio</h2>", unsafe_allow_html=True)
    st.markdown("<div class='content'>", unsafe_allow_html=True)

    # Add button to add a new project
    if st.button("Add Project"):
        project_form()

    # Show existing projects
    projects = get_projects()
    for project in projects:
        render_project(project)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# Render project block
def render_project(project):
    st.markdown("<div class='portfolio-item'>", unsafe_allow_html=True)
    st.markdown("<h3 class='portfolio-item-title'>{}</h3>".format(project["name"]), unsafe_allow_html=True)
    st.markdown("<p class='portfolio-item-description'>{}</p>".format(project["description"]), unsafe_allow_html=True)
    st.markdown("<a class='portfolio-item-link' href='{}' target='_blank'>View Project</a>".format(project["link"]), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# Render project form
def project_form():
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)

    st.markdown("<h3 class='title'>Add Project</h3>", unsafe_allow_html=True)

    # Project name input
    name = st.text_input("Project Name", key="project_name")

    # Project description input
    description = st.text_area("Project Description", key="project_description")

    # Save button
    if st.button("Save Project"):
        # Fetch image and link from Google Custom Search API
        image_url, link = fetch_project_image(name)

        # Create project dictionary
        project = {
            "name": name,
            "description": description,
            "image_url": image_url,
            "link": link,
        }

        # Add project to the list of projects
        add_project(project)

        # Show success message
        st.success("Project saved successfully!")

    st.markdown("</div>", unsafe_allow_html=True)


# Fetch project image and link from Google Custom Search API
def fetch_project_image(project_name):
    # Configure Google Custom Search API
    api_key = "YOUR_API_KEY"
    cx = "YOUR_CX"
    search_query = project_name

    # Make API request
    response = requests.get(
        "https://www.googleapis.com/customsearch/v1",
        params={"key": api_key, "cx": cx, "q": search_query, "searchType": "image"},
    )
    data = response.json()

    # Extract image URL and link
    if "items" in data and len(data["items"]) > 0:
        image_url = data["items"][0]["link"]
        link = data["items"][0]["image"]["contextLink"]
    else:
        image_url = ""
        link = ""

    return image_url, link


# Get existing projects from the database
def get_projects():
    # TODO: Implement fetching projects from the database
    # Placeholder data for demonstration
    return [
        {
            "name": "Project 1",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image_url": "https://example.com/project1.jpg",
            "link": "https://example.com/project1",
        },
        {
            "name": "Project 2",
            "description": "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "image_url": "https://example.com/project2.jpg",
            "link": "https://example.com/project2",
        },
    ]


# Add a project to the database
def add_project(project):
    # TODO: Implement saving the project to the database
    # Placeholder implementation for demonstration
    pass


# Page: Certifications
def certifications_page():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='title'>Certifications</h2>", unsafe_allow_html=True)
    st.markdown("<div class='content'>", unsafe_allow_html=True)
    st.write("- [Microsoft Az-900](https://www.credly.com/badges/4429568b-8f97-424b-919c-5ae36e2617ae/linked_in_profile)")
    st.image("/home/keshav/Desktop/Az900.png", use_column_width=True, caption="Microsoft Az-900 Certification")
    # Add more certifications here
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# Page: Skills
def skills_page():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='title'>Skills</h2>", unsafe_allow_html=True)
    st.markdown("<div class='content'>", unsafe_allow_html=True)
    st.write("- Skill 1")
    st.write("- Skill 2")
    st.write("- Skill 3")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# Page: Upload Photo
def upload_photo_page():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='title'>Upload Photo</h2>", unsafe_allow_html=True)
    st.markdown("<div class='content'>", unsafe_allow_html=True)
    # Add code for uploading photo here
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# Navigation
pages = {
    "Home": home_page,
    "Portfolio": portfolio_page,
    "Certifications": certifications_page,
    "Skills": skills_page,
    "Upload Photo": upload_photo_page,
}

# Render navigation bar
st.markdown("<div class='navbar'>", unsafe_allow_html=True)
st.markdown("<a class='navbar-brand' href='#home'>My Portfolio</a>", unsafe_allow_html=True)
st.markdown("<ul class='nav-links'>", unsafe_allow_html=True)

# Render navigation links
for page in pages.keys():
    st.markdown(f"<li><a href='#{page.replace(' ', '-').lower()}' class='nav-link'>{page}</a></li>", unsafe_allow_html=True)

st.markdown("</ul></div>", unsafe_allow_html=True)

# Render page content
for page, page_func in pages.items():
    st.markdown(f"<h2 id='{page.replace(' ', '-').lower()}'>{page}</h2>", unsafe_allow_html=True)
    page_func()

# Display LinkedIn profile link
st.markdown("LinkedIn Profile: [Keshav Bajaj](https://www.linkedin.com/in/keshavbajaj03/)")
