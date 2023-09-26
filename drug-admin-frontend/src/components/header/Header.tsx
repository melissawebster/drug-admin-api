// import './Header.css';
import logo from '../../assets/logo.png';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Header.css'

function Header () {
    return (
        <>
          <div className="header container-fluid">
            <div className="row">
              <div className="col-8 mx-auto d-flex">
                  <img src={logo} alt="logo" className="logo"/>
                  <div className="title">Drug Admin</div>
              </div>
            </div>
          </div>
        </>
      )
}

export default Header