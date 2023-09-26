import 'bootstrap/dist/css/bootstrap.min.css';
import './SearchBar.css'

function SearchBar () {
    return (
        <>
          <div className="search-bar container-fluid mt-5">

            <div className="row">
              <div className="col-8 mx-auto d-flex">
                Search for a drug
              </div>
            </div>

            <div className="row pt-2">
              <div className="col-8 mx-auto d-flex">
                  <input type="text" className="text-input" placeholder=" Type here..." />
                  <button className="button mx-3">Go</button>
                  <p>or</p>
                  <button className="button mx-3">Get all</button>
              </div>
            </div>

            <div className="row">
              <div className="col-8 mx-auto d-flex">
              <button className="button mt-3">Add new</button>
              </div>
            </div>

          </div>
        </>
      )
}

export default SearchBar