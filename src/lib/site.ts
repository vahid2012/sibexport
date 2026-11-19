export const SITE = {
  name: 'SibExport',
  domain: 'https://sibexport.ir',
  tagline: 'From Iranian Orchards to Global Markets',
  supportingTagline: 'Premium Iranian Apples for Global Markets',
  description:
    'SibExport is an Iranian apple sourcing and wholesale export supplier. Premium red, golden and green Iranian apples for international importers, distributors and wholesale buyers.',
} as const;

export const CONTACT = {
  whatsappNational: '09143403431',
  whatsappInternational: '+989143403431',
  whatsappUrl: 'https://wa.me/989143403431',
  phoneNational: '04433465524',
  phoneInternational: '+984433465524',
  phoneUrl: 'tel:+984433465524',
  email: 'sanat.abr@gmail.com',
  emailUrl: 'mailto:sanat.abr@gmail.com',
  address:
    'Akay Trade Office, Tila Street, Azadegan Street, Urmia, West Azerbaijan, Iran.',
} as const;

export const SOCIAL = {
  facebook: 'https://www.facebook.com/share/18aBjqpNMT/',
  instagram:
    'https://www.instagram.com/iran.sourcing.hub?lqvp=MTFqMmIyajhub2F6cQ==',
  linkedin:
    'https://www.linkedin.com/in/vahid-gholipour-81a13996?utm_source=share_via&utm_content=profile&utm_medium=member_android',
} as const;

export type NavLink = {
  label: string;
  href: string;
};

export const NAV_LINKS: NavLink[] = [
  { label: 'Home', href: '/' },
  { label: 'About', href: '/about/' },
  { label: 'Apple Varieties', href: '/iranian-apple-varieties/' },
  { label: 'Quality', href: '/apple-quality-specifications/' },
  { label: 'Packaging', href: '/apple-packaging/' },
  { label: 'Export Process', href: '/apple-export-process/' },
  { label: 'Destinations', href: '/export-destinations/' },
  { label: 'FAQ', href: '/faq/' },
  { label: 'Blog', href: '/blog/' },
  { label: 'Contact', href: '/contact/' },
];

export const FOOTER_COMPANY_LINKS: NavLink[] = [
  { label: 'About SibExport', href: '/about/' },
  { label: 'Export Destinations', href: '/export-destinations/' },
  { label: 'Export Process', href: '/apple-export-process/' },
  { label: 'Export Insights', href: '/blog/' },
  { label: 'Contact Us', href: '/contact/' },
];

export const FOOTER_PRODUCT_LINKS: NavLink[] = [
  { label: 'Iranian Apple Varieties', href: '/iranian-apple-varieties/' },
  { label: 'Red Apple Export', href: '/red-apple-export/' },
  { label: 'Golden Apple Export', href: '/golden-apple-export/' },
  { label: 'Green Apple Export', href: '/green-apple-export/' },
  { label: 'Quality & Specifications', href: '/apple-quality-specifications/' },
  { label: 'Apple Packaging', href: '/apple-packaging/' },
];

export const FOOTER_SUPPORT_LINKS: NavLink[] = [
  { label: 'Request a Quotation', href: '/request-a-quotation/' },
  { label: 'Frequently Asked Questions', href: '/faq/' },
  { label: 'Privacy Policy', href: '/privacy-policy/' },
];

export type Breadcrumb = {
  label: string;
  href?: string;
};
