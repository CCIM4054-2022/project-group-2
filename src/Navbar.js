export default function Navbar() {
    return <nav className="nav">
        <a href ="/" className="site-title">Snake VS Snake</a>
        <ul>
            <CustomLink href="/">Create Game</CustomLink>
            <CustomLink href="/spectategame">Spectate Game</CustomLink>
            <CustomLink href="/viewscoreboard">Scoreboard</CustomLink>
        </ul>
    </nav>

function CustomLink({ href, children,...props }) {
    const path = window.location.pathname
    return(
        <li className={path === href ? "active" : ""}>
            <a href={href} {...props}>{children}</a>
        </li>
    )
}

}