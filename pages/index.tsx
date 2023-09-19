import '@/public/globals.css'
import Link from "next/link";
import type { Metadata } from 'next'
export const metadata: Metadata = {
    title: 'Home',
    description: 'Home page',
    keywords: 'Home, Next.js, TypeScript',
}

export default function Home() {
    return (
        <div>
            <main className="flex min-h-screen flex-col items-center p-24 mb-2">
                <p>Hello World</p>
                <button><Link href={'/login'}>Login</Link></button>
            </main>
        </div>
    )
}