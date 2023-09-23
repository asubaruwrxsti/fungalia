import { useRouter } from "next/navigation";
export default function LoginForm() {
    const router = useRouter();
    return (
        <form
            className="flex flex-col items-center justify-center border border-gray-400 p-8 rounded-md"
            onSubmit={async (e) => {
                e.preventDefault();
                let username = (document.getElementById('username') as HTMLInputElement).value;
                let password = (document.getElementById('password') as HTMLInputElement).value;
                let response = await fetch('/api/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({username, password})
                });
                response = await response.json();
                if (response.status) {
                    console.log(response);
                }
            }}
        >
            <input
                className="border border-gray-400 p-2 mt-1 rounded-md"
                type="text" placeholder="username" id={"username"}
            />
            <input
                className="border border-gray-400 p-2 mt-1 rounded-md"
                type="password" placeholder="password" id={"password"}
            />
            <button
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 mt-3 rounded"
                type="submit">Login</button>
        </form>
    )
}