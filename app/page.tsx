import Link from "next/link";
import '@/public/globals.css'
export default function Home() {
  return (
      <div>
        <div className="name">Hello World</div>
        <button><Link href={"/login"}>Go To Login</Link></button>
      </div>
  )
}
