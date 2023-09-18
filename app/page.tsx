import Link from "next/link";
import RootLayout from '@/app/layout';
import '@/public/globals.css'
export default function Home() {
  return (
      <RootLayout>
          <div>
                <div className="name">Hello World</div>
                <button><Link href={"/login"}>Go To Login</Link></button>
          </div>
      </RootLayout>
  )
}
