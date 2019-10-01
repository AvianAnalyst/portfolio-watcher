<template>
    <div class="table">
        <table>
            <tr>
                <th>Company</th>
                <th>Cost</th>
                <th>Shares</th>
            </tr>
            <tr v-bind:key="row.name" v-for="row in data">
                <td v-bind:key="col" v-for="col in row">{{col}}</td>
            </tr>
        </table>
    </div>
</template>

<script>
    export default {
        props: {
            data: Array
        },
    };
</script>

<style scoped>
    <div> {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
