import axios from 'axios';

const apiClient = axios.create({
    headers: {
        "Content-Type": 'application/json'
    },
    baseURL: 'http://localhost:8010'
});

const { get, post, put, patch, delete: destroy } = apiClient;
export { get, post, put, patch, destroy };