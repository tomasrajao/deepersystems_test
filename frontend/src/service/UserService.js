import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/users';

export async function getUsersData() {
    try {
        const { data } = await axios.get(API_URL);
        return data;
    } catch (error) {
        console.error('Error fetching users:', error);
        throw error;
    }
};
export async function getUser(id) {
    try {
        const { data } = await axios.get($`{API_URL}/{id}`);;
        return data;
    } catch (error) {
        console.error('Error fetching users:', error);
        throw error;
    }
};
export async function createUser() {
    try {
        const { data } = await axios.post(API_URL);;
        return data;
    } catch (error) {
        console.error('Error fetching users:', error);
        throw error;
    }
};
export async function updateUser(id, user) {
    try {
        const { data } = await axios.put($`{API_URL}/{id}`, user);;
        return data;
    } catch (error) {
        console.error('Error fetching users:', error);
        throw error;
    }
};
export async function deleteUser(id) {
    try {
        const { data } = await axios.delete($`{API_URL}/{id}`);;
        return data;
    } catch (error) {
        console.error('Error fetching users:', error);
        throw error;
    }
}