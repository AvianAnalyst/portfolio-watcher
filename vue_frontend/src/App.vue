<template>
    <div id="app">
        <ReportPicker />
        <Table v-if="data" v-bind:data="data" />
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
        data(){
            return {
                data: null,
            };
        },
        async created() {
            const data = await fetch('http://localhost:8000/investments');
            this.data = await data.json();
            // eslint-disable-next-line no-console
            console.log(this.data);
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
