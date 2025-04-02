import './index.css'

const Header = () => {

    const menus = [
        'Home',
        'Stories',
        'Works',
        'Pages',
        'Contact'
    ]


    return (
        <header>
            <h2 className="logo">Le Khanh Toan</h2>
            {
                menus.map((item, idx) => (
                    <p key={idx} className="menu-item">{item}</p>    
                ))
            }
        </header>
    )
}

export default Header;