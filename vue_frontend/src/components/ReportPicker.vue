<template>
    <div class="report">
        <form method="get" target="http://localhost:8000/investments">
            <input type="date">
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
    export default {
        name: "report",
    };
</script>

<style>
    .report {
        text-align: center;
    }
</style>
