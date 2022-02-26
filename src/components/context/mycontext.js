import React, { useState, useEffect,useContext} from 'react';
import { Children } from 'react';
import { useHistory } from 'react-router-dom';

const homeContext=React.createContext();
const aboutContext=React.createContext();
const portfolioContext=React.createContext();
const contactContext=React.createContext();
const loadContext = React.createContext();

export {homeContext,aboutContext,portfolioContext,contactContext,loadContext};

function ApiContext(props) {

    const [homedata, setHomeData] = useState([]);
    const [aboutdata, setAboutData] = useState([]);
    const [portfoliodata, setPortfolioData] = useState([]);
    const [contactdata, setContactData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

  

    const url1 = "http://127.0.0.1:8000/home/";

    const url2 = "http://127.0.0.1:8000/about/";

    const url3 = "http://127.0.0.1:8000/portfolio/";

    const url4 = "http://127.0.0.1:8000/contact/";


    useEffect(() => {
        fetch(url1)
            .then(res => res.json())
            .then(
                (result) => {
                    setHomeData(result);
                    setLoading(false);
                },
                (error) => {
                    setError(error);
                    setLoading(false);
                }
            )
    }, []);

    useEffect(() => {
        fetch(url2)
            .then(res => res.json())
            .then(
                (result) => {
                    setAboutData(result);
                    setLoading(false);
                },
                (error) => {
                    setError(error);
                    setLoading(false);
                }
            )
    }, []);

    useEffect(() => {
        fetch(url3)
            .then(res => res.json())
            .then(
                (result) => {
                    setPortfolioData(result);
                    setLoading(false);
                },
                (error) => {
                    setError(error);
                    setLoading(false);
                }
            )
    }, []);

    useEffect(() => {
        fetch(url4)
            .then(res => res.json())
            .then(
                (result) => {
                    setContactData(result);
                    setLoading(false);
                },
                (error) => {
                    setError(error);
                    setLoading(false);
                }
            )
    }, []);

  return (
    <div>
        <homeContext.Provider value={[homedata, setHomeData]} >
            <aboutContext.Provider value={[aboutdata, setAboutData]}>
                <portfolioContext.Provider value={[portfoliodata, setPortfolioData]}>
                    <contactContext.Provider value={[contactdata, setContactData]}>
                        <loadContext.Provider value={[loading, setLoading]}>
                        {props.children}
                        </loadContext.Provider>
                    </contactContext.Provider>
                </portfolioContext.Provider>
            </aboutContext.Provider>
        </homeContext.Provider>
    </div>
  );
}
   
export default ApiContext;