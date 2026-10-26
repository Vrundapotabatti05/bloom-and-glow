import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Bloom & Glow - Premium Gift Shop",
  description: "Premium Gifts for Every Special Occasion",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
