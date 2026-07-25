"""Central content source for the portfolio (mirrors the resume)."""

PERSONAL = {
    "name": "Oyeleke Azeezat Bisola",
    "first_name": "Azeezat",
    "title": "Administrative Professional",
    "subtitle": "Office Management & Coordination Specialist",
    "email": "azeezafunmi@gmail.com",
    "phone": "+234 813 938 6610",
    "phone_href": "+2348139386610",
    "location": "Ogun State, Nigeria",
    "linkedin": "https://www.linkedin.com/in/azeezat-oyeleke",
    "intro": (
        "A detail-oriented and proactive graduate with strong organizational, "
        "leadership, and administrative skills developed through academic, "
        "professional, and union leadership roles. I help organizations run "
        "smoothly through efficient office management, accurate records handling, "
        "and seamless staff coordination."
    ),
}

ABOUT = {
    "paragraphs": [
        "I am a detail-oriented and proactive graduate of Agriculture (B.Sc. "
        "Fisheries), currently serving in the National Youth Service Corps (NYSC). "
        "Over the years I have built a solid foundation in administration through "
        "hands-on experience in office coordination, documentation, and team "
        "leadership.",
        "My goal is to contribute to efficient office management, meticulous "
        "records handling, and effective staff coordination. I thrive in "
        "structured environments where organization, clear communication, and "
        "initiative make a measurable difference.",
    ],
    "highlights": [
        {"value": "6+", "label": "Administrative & Leadership Roles"},
        {"value": "8+", "label": "Years of Coordination Experience"},
        {"value": "100%", "label": "Commitment to Excellence"},
    ],
    "focus_areas": [
        {
            "icon": "clipboard",
            "title": "Office Management",
            "text": "Streamlining workflows, documentation, and daily operations.",
        },
        {
            "icon": "sparkles",
            "title": "Records Handling",
            "text": "Accurate data entry, registries, and confidential record-keeping.",
        },
        {
            "icon": "users",
            "title": "Staff Coordination",
            "text": "Aligning teams, correspondence, and cross-committee activities.",
        },
    ],
}

EDUCATION = [
    {
        "school": "Usmanu Danfodiyo University, Sokoto",
        "qualification": "B.Sc. Agriculture (Fisheries)",
        "year": "2024",
    },
    {
        "school": "Federal Polytechnic Offa Staff Secondary School",
        "qualification": "Senior Secondary Certificate",
        "year": "2014",
    },
    {
        "school": "Nawair-ud-Deen Nursery & Primary School, Offa",
        "qualification": "First School Leaving Certificate",
        "year": "2008",
    },
]

EXPERIENCE = [
    {
        "role": "Administrative Assistant (NYSC)",
        "company": "Life Transforming College, Ogun State",
        "period": "Nov 2025 – Present",
        "current": True,
        "points": [
            "Facilitate academic and administrative synergy throughout the college.",
            "Oversee student data management, documentation, and clerical registries.",
            "Regulate office workflows while assisting leadership and personnel.",
            "Enhance internal correspondence and streamline routine organizational tasks.",
        ],
    },
    {
        "role": "Intern",
        "company": "Rahama Farms, Offa, Kwara State",
        "period": "400 Level Internship · 2023",
        "current": False,
        "points": [
            "Assisted in daily farm administration and documentation of operations.",
            "Supported supervisors in coordinating agricultural schedules and resources.",
        ],
    },
    {
        "role": "Vice President (Administration)",
        "company": "Offa Student Union, UDUS",
        "period": "2023",
        "current": False,
        "points": [
            "Managed administrative correspondence and documentation for the student union.",
            "Coordinated activities across multiple committees to ensure smooth operations.",
        ],
    },
    {
        "role": "Treasurer",
        "company": "Offa Student Union, UDUS",
        "period": "2022",
        "current": False,
        "points": [
            "Maintained accurate financial records and reports.",
            "Supported the executive body in planning and organizing events.",
        ],
    },
    {
        "role": "Teacher / Administrative Assistant",
        "company": "Ideal Primary School, Offa",
        "period": "2022",
        "current": False,
        "points": [
            "Handled record-keeping, timetabling, and student data management.",
            "Assisted in classroom coordination and administrative duties.",
        ],
    },
    {
        "role": "Administrative Assistant",
        "company": "Kimbo Catering Services, Kaduna State",
        "period": "2017 – 2020",
        "current": False,
        "points": [
            "Supported daily operations and staff coordination.",
            "Managed bookings, scheduling, and basic record-keeping.",
        ],
    },
]

SKILLS = [
    {"name": "Administrative Support & Office Management", "level": 95},
    {"name": "Record Keeping & Data Entry", "level": 92},
    {"name": "Leadership & Coordination", "level": 90},
    {"name": "Financial Documentation", "level": 85},
    {"name": "Communication & Team Collaboration", "level": 93},
    {"name": "Problem Solving & Initiative", "level": 88},
]

ACHIEVEMENTS = [
    {
        "title": "Vice President (Administration)",
        "org": "Offa Student Union, UDUS",
        "description": (
            "Led administrative operations for the union, managing correspondence "
            "and coordinating multiple committees for smooth execution of activities."
        ),
    },
    {
        "title": "Treasurer",
        "org": "Offa Student Union, UDUS",
        "description": (
            "Maintained accurate financial records and supported the executive body "
            "in planning and organizing union events."
        ),
    },
    {
        "title": "Cross-Committee Coordination",
        "org": "Student Leadership",
        "description": (
            "Coordinated activities across diverse teams, ensuring timely "
            "communication and consistent organizational impact."
        ),
    },
    {
        "title": "Records & Data Management",
        "org": "Multiple Institutions",
        "description": (
            "Built a track record of meticulous documentation, registry management, "
            "and student data handling across schools and colleges."
        ),
    },
]

INTERESTS = [
    "Reading and Writing Novels",
    "Public Speaking",
    "Effective Communication",
]

NAV_LINKS = [
    {"label": "Home", "href": "#home"},
    {"label": "About", "href": "#about"},
    {"label": "Education", "href": "#education"},
    {"label": "Experience", "href": "#experience"},
    {"label": "Skills", "href": "#skills"},
    {"label": "Achievements", "href": "#achievements"},
    {"label": "Contact", "href": "#contact"},
]


def get_context():
    """Return all content for template rendering."""
    return {
        "personal": PERSONAL,
        "about": ABOUT,
        "education": EDUCATION,
        "experience": EXPERIENCE,
        "skills": SKILLS,
        "achievements": ACHIEVEMENTS,
        "interests": INTERESTS,
        "nav_links": NAV_LINKS,
    }
