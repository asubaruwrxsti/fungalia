import { Inter } from 'next/font/google'
import React from "react";

const inter = Inter({ subsets: ['latin'] })
export const metadata = {
    title: 'Login',
    description: 'Generated by create next pages',
}

export default function RootLayout({children}: {children: React.ReactNode}) {
    return (
        <html lang="en">
            <body className={inter.className}>{children}</body>
        </html>
    )
}
