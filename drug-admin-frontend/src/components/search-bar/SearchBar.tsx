import 'bootstrap/dist/css/bootstrap.min.css';
import './SearchBar.css'
import Table from '../table/Table';
import { useState } from 'react'
import axios from 'axios'

function SearchBar () {

  const [name, setName] = useState('')

  const fetchDataByName = () => {
    axios.get(`http://127.0.0.1:8000/drugs/get_by_name/${name}`)
      .then(res => setData(res.data))
      .catch(err => console.log(err))
  }

  const [data, setData] = useState<any[]>([])

  const fetchAllData = () => {
    axios.get('http://127.0.0.1:8000/drugs/')
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
            <input 
              type="text" 
              className="text-input" 
              maxLength={50} 
              placeholder=" Type here..." 
              value={name} 
              onChange={(e) => setName(e.target.value)}
            />
            <button className="button mx-3" onClick={fetchDataByName}>Go</button>
            <span>or</span>
            <button className="button mx-3" onClick={fetchAllData}>Get&nbsp;all</button>
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
