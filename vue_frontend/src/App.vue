<template>
    <div id="app" class="container">
        <h1>Investments through:</h1>
        <ReportPicker v-on:change="updateReportDate" />
        <h1>Data through:</h1>
        <ReportPicker v-on:change="updateInfoDate" />
        <Table v-bind:data="investments" class="col-md"/>
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
            async updateReportDate(date) {
                this.report_date = date;
                // eslint-disable-next-line no-console
                console.log('updating investments');
                await this.updateInvestments()
            },
            async updateInfoDate(date) {
                this.info_date = date;
                // eslint-disable-next-line no-console
                console.log('updating investments');
                await this.updateInvestments()
            },
            async updateInvestments() {
                let url = 'http://localhost:8000/investments';
                if (this.report_date) {
                    url += '?investment_date=' + this.report_date + '&';
                }
                if (this.info_date) {
                    url += 'info_date=' + this.info_date;
                }
                const investments = await fetch(url);
                this.investments = await investments.json();
                // eslint-disable-next-line no-console
                console.log(this.investments);
                // eslint-disable-next-line no-console
                console.log('updating investments with ' + url)
            },
            makeUrl() {
                switch (this.info_date + this.report_date) {
                    case 0:
                        this.url = 'http://localhost:8000/investments';
                        break;
                    case 1:
                        this.url = 'http://localhost:8000/investments?';
                        if (this.report_date) {
                            this.url += 'investment_date=' + this.report_date;
                        } else {
                            this.url += 'info_date=' + this.info_date;
                        }
                        break;
                    case 2:
                        this.url = 'http://localhost:8000/investments?investment_date=' +
                                    this.report_date + '&info_date=' + this.info_date;
                }
            }
        },
        data(){
            return {
                investments: null,
                report_date: null,
                info_date: null,
                url: null,
            };
        },
        async created() {
            await this.updateInvestments()
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
