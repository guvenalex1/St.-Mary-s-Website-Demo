# St. Mary's Academy Website

A modern, professional website for St. Mary's Academy - a PK-12 Catholic school that emphasizes academic excellence, faith formation, and character development.

## Features

### Design Elements
- **Color Scheme**: Subtle integration of red and blue colors throughout the design
- **Typography**: Elegant combination of Playfair Display (headings) and Inter (body text)
- **Modern Layout**: Clean, sophisticated design appropriate for middle and high school audiences
- **Responsive Design**: Fully responsive across all devices

### Key Sections
1. **Hero Section**: Compelling introduction with school motto "One School Serving All" and "Magnify your Knowledge"
2. **Quick Stats**: Key metrics about the school (PK-12, years of excellence, college acceptance rate, student-teacher ratio)
3. **Academic Excellence**: Detailed information about Elementary, Middle, and High School programs
4. **Why Choose SMA**: Faith-centered education, academic excellence, strong community, innovation & technology
5. **Campus Life**: Athletics, Arts, Student Activities, Service Learning
6. **Call to Action**: Visit scheduling and application prompts

### Navigation Structure
- **Discover SMA**: About Us, Faculty & Staff, Spiritual Life, Center for Innovation, Giving
- **Admissions**: Apply Now, Visit, Tuition & Financial Aid, FAQ
- **Academics**: High School, Middle School, Elementary, STEM Programs
- **Campus Life**: Athletics, Arts, Student Activities, House System
- **Current Families**: Resources and information for existing families

## Technical Implementation

### HTML Structure
- Semantic HTML5 elements
- Accessible navigation with ARIA labels
- SEO-optimized meta tags and structure
- Mobile-first responsive design

### CSS Features
- CSS Grid and Flexbox for modern layouts
- CSS Custom Properties (variables) for consistent theming
- Smooth transitions and hover effects
- Mobile-responsive navigation
- Gradient backgrounds using school colors

### JavaScript Functionality
- Mobile menu toggle
- Smooth scrolling navigation
- Header scroll effects
- Dropdown menu interactions
- Scroll-triggered animations
- Counter animations for statistics
- Accessibility enhancements
- Performance optimizations

## Color Palette

### Primary Colors
- **Primary Red**: #C41E3A (St. Mary's red)
- **Primary Blue**: #1E3A8A (St. Mary's blue)
- **Light Red**: #EF4444 (accent red)
- **Light Blue**: #3B82F6 (accent blue)
- **Dark Red**: #991B1B (deep red)
- **Dark Blue**: #1E40AF (deep blue)

### Neutral Colors
- **White**: #FFFFFF
- **Light Gray**: #F8FAFC
- **Medium Gray**: #64748B
- **Dark Gray**: #334155
- **Black**: #0F172A

## File Structure

```
st-marys-academy/
├── index.html              # Main homepage
├── css/
│   └── style.css          # Main stylesheet
├── js/
│   └── main.js           # JavaScript functionality
├── images/               # Image assets (placeholder images)
│   ├── st-marys-logo.png
│   ├── hero-campus.jpg
│   ├── elementary-students.jpg
│   ├── middle-school-students.jpg
│   ├── high-school-students.jpg
│   ├── students-learning.jpg
│   ├── athletics.jpg
│   ├── arts-program.jpg
│   ├── student-activities.jpg
│   └── service-learning.jpg
└── README.md            # This documentation
```

## Responsive Breakpoints

- **Desktop**: 1024px and above
- **Tablet**: 768px - 1023px
- **Mobile**: 767px and below
- **Small Mobile**: 480px and below

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- iOS Safari (latest)
- Chrome Mobile (latest)

## Performance Features

- Optimized CSS with minimal redundancy
- Efficient JavaScript with event delegation
- Lazy loading for images
- Smooth animations with CSS transforms
- Debounced scroll events
- Service Worker ready for PWA implementation

## Accessibility Features

- Semantic HTML structure
- ARIA labels and roles
- Keyboard navigation support
- Focus management
- Screen reader friendly
- High contrast color ratios
- Skip to content links

## Future Enhancements

1. **Content Management**: Integration with a CMS for easy content updates
2. **Search Functionality**: Site-wide search capability
3. **Event Calendar**: School events and important dates
4. **News Section**: School news and announcements
5. **Photo Gallery**: School life and event photos
6. **Online Applications**: Integrated application forms
7. **Parent Portal**: Secure access for current families
8. **Multi-language Support**: Spanish and Vietnamese translations
9. **Progressive Web App**: Offline functionality and app-like experience
10. **Analytics Integration**: Google Analytics for visitor tracking

## Installation & Setup

1. Clone or download the website files
2. Ensure all files are in the correct directory structure
3. Replace placeholder images with actual school photos
4. Update contact information and school-specific details
5. Test across different devices and browsers
6. Deploy to web hosting service

## Customization

### Colors
Update the CSS custom properties in `:root` to change the color scheme:

```css
:root {
    --primary-red: #C41E3A;
    --primary-blue: #1E3A8A;
    /* ... other color variables */
}
```

### Typography
Change fonts by updating the font imports and variables:

```css
:root {
    --font-primary: 'Playfair Display', serif;
    --font-secondary: 'Inter', sans-serif;
}
```

### Content
Update the HTML content in `index.html` and create additional pages as needed for the complete website structure.

## Contact

For questions about this website implementation, please contact the development team.

---

*This website was created to showcase St. Mary's Academy's commitment to academic excellence, faith formation, and community building in a modern, accessible format.*
