<template>
    <div id="app" class="container">
        <ReportPicker v-on:change="updateDate" />
        <Table v-bind:data="data" class="col-md"/>
    </div>
</template>

<script>
    import Table from "./components/Table";
    import ReportPicker from "./components/ReportPicker";

    export default {
        name: 'app',
        components: {
            Table,
            ReportPicker
        },
        methods: {
            async updateDate(date) {
                this.date = date;
                // eslint-disable-next-line no-console
                console.log('updating date');
                await this.updateData()
            },
            async updateData() {
                let url = 'http://localhost:8000/investments';
                if (this.date) {
                    url += '?investment_date=' + this.date;
                }
                const data = await fetch(url);
                this.data = await data.json();
                // eslint-disable-next-line no-console
                console.log(this.data);
                // eslint-disable-next-line no-console
                console.log('updating data with ' + url)
            },
        },
        data(){
            return {
                data: null,
                date: null,
            };
        },
        async created() {
            await this.updateData()
        },
    }

</script>

<style>
    @import "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css";
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
