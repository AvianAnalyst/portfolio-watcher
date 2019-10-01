<template>
    <div class="table">
        <table class="table table-bordered table-striped text-center">
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

