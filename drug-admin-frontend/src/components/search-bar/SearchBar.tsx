import 'bootstrap/dist/css/bootstrap.min.css';
import './SearchBar.css'
import Table from '../table/Table';
import { useState } from 'react'
import axios from 'axios'

// function FetchAllData() {
//     const [data, setData] = useState<any[]>([])

//     const fetchAllDataOnClick = () => {
//       axios.get('http://127.0.0.1:8000/drugs')
//         .then(res => setData(res.data))
//         .catch(err => console.log(err))
//     }

// }

function SearchBar () {

  const [data, setData] = useState<any[]>([])

  const fetchAllDataOnClick = () => {
    axios.get('http://127.0.0.1:8000/drugs')
      .then(res => setData(res.data))
      .catch(err => console.log(err))
  }

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
                <span>or</span>
                <button className="button mx-3" onClick={fetchAllDataOnClick}>Get&nbsp;all</button>
            </div>
          </div>

          <div className="row">
            <div className="col-8 mx-auto d-flex">
            <button className="button mt-3">Add new</button>
            </div>
          </div>

          <Table data={data} />

        </div>
      </>
    )
}

export default SearchBar