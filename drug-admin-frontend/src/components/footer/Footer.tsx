import 'bootstrap/dist/css/bootstrap.min.css'
import './Footer.css'

function Footer () {
    return (
        <>
          <div className="footer container-fluid fixed-bottom">
            <div className="row">
                <div className="col-8 mx-auto pt-3">
                Developed by Melissa Webster
                <br />
                GitHub: <a href="https://github.com/melissawebster/" target="_blank">@melissawebster</a>
                </div>
            </div>
          </div>
        </>
      )
}

export default Footer