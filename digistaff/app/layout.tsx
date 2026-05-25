import type { Metadata } from "next";
import {
  Space_Grotesk,
  Manrope,
  Cormorant_Garamond,
  JetBrains_Mono,
} from "next/font/google";
import "./globals.css";

const spaceGrotesk = Space_Grotesk({
  subsets: ["latin", "latin-ext"],
  weight: ["400", "500", "600", "700"],
  variable: "--font-sans",
  display: "swap",
});

const manrope = Manrope({
  subsets: ["latin", "latin-ext"],
  weight: ["400", "500", "600", "700"],
  variable: "--font-body",
  display: "swap",
});

const cormorant = Cormorant_Garamond({
  subsets: ["latin", "latin-ext"],
  weight: ["400", "500"],
  style: ["italic"],
  variable: "--font-serif",
  display: "swap",
});

const jetbrainsMono = JetBrains_Mono({
  subsets: ["latin", "latin-ext"],
  weight: ["400", "500"],
  variable: "--font-mono",
  display: "swap",
});

const siteUrl = "https://digistaff.ru";
const title = "Digistaff — аутстаффинг IT-специалистов за 3–7 дней";
const description =
  "Подбор backend, frontend, DevOps, QA, mobile, data, 1С специалистов в действующую команду за 3–7 дней. Тех-отбор и замена на нашей стороне.";

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title,
  description,
  applicationName: "Digistaff",
  alternates: { canonical: "/" },
  openGraph: {
    type: "website",
    locale: "ru_RU",
    url: siteUrl,
    siteName: "Digistaff",
    title,
    description,
  },
  twitter: {
    card: "summary_large_image",
    title,
    description,
  },
  robots: { index: true, follow: true },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      lang="ru"
      className={`${spaceGrotesk.variable} ${manrope.variable} ${cormorant.variable} ${jetbrainsMono.variable}`}
    >
      <body>
        {children}
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify([
              {
                "@context": "https://schema.org",
                "@type": "Organization",
                name: "Digistaff",
                url: siteUrl,
                description,
              },
              {
                "@context": "https://schema.org",
                "@type": "Service",
                serviceType: "IT staff augmentation / outstaffing",
                provider: { "@type": "Organization", name: "Digistaff" },
                areaServed: "RU",
                description,
              },
            ]),
          }}
        />
      </body>
    </html>
  );
}
