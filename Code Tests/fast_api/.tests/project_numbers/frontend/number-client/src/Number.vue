<template>
    <div>
       <h1>ATUAL NUMBER: {{ value }}</h1>
       <form @submit.prevent="updateCurrentNumber">
           <input v-model="new_value" placeholder="NEW NUMBER">
           <button type="SUBMIT">update</button>
       </form>
    </div>
</template>

<script>
export default {
    name: 'Number',
    data: () => {
        return {
            value: null
        }
    },
    methods: {
        async getCurrentNumber() {
            let response = await fetch('http://localhost:8000/number', {method: 'get'})
            if (response.ok) {
                let resp = await response.json()
                this.value = resp.number.value
                return
            }
            this.value = "could not load from server"
            return
        },
        async updateCurrentNumber() {
            if (this.new_value === null) {
                return  
              } // checking for null and 0 values
          
            fetch('http://localhost:8000/number',
            {
                 method: 'post',
                 body: JSON.stringify({
                   value: this.new_value
                 }),
                 headers: {"Content-type": "application/json"}
            }).then(() => this.refreshPage()).catch(
                err => console.error(err)
            );
          return
       },
       refreshPage() {
          location.reload()
       },
    },
    mounted() {
        this.getCurrentNumber();
    },
}
</script>
<style scoped></style>
