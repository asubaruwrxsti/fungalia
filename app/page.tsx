import Link from "next/link";

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