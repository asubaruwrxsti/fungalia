import React from "react";

export default function Login() {
    return <main>
        <form action="/api/login" method="post">
            <input type="text" placeholder="username"/>
            <input type="password" placeholder="password"/>
            <button type="submit">Login</button>
        </form>
    </main>
}